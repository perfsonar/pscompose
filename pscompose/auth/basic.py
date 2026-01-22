import bcrypt

from sqlalchemy.orm import sessionmaker
from fastapi import Depends, HTTPException
from pscompose.settings import TOKEN_SCOPES
from pscompose.models import User, UserTable, engine
from fastapi.security import HTTPBasic, HTTPBasicCredentials, SecurityScopes


class BasicBackend:
    def __init__(self):
        UserTable.__table__.create(bind=engine, checkfirst=True)
        self.session = sessionmaker(bind=engine)()
        if not self.session.query(UserTable).filter_by(id=1).first():
            self.create_user(
                email="admin",
                name="Administration User",
                password="admin",
                scopes=[s for s in TOKEN_SCOPES.values()],
            )

    def query(self, username=None, limit=10):
        query = self.session.query(UserTable)
        if username:
            query = query.filter_by(username=username)
        if limit:
            query = query.limit(limit)
        rows = query.all()
        return rows

    def get_user(self, username, password):
        db_user = self.session.query(UserTable).filter_by(username=username).first()
        if db_user and bcrypt.checkpw(password.encode(), db_user.password):
            return User(
                username=db_user.username,
                email=db_user.username,
                name=db_user.name,
                scopes=db_user.scopes,
                favorites=db_user.favorites,
            )
        else:
            raise HTTPException(status_code=401, detail="Invalid user")

    def create_user(self, email, name, password, scopes):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        new_user = UserTable(username=email, name=name, password=hashed_password, scopes=scopes)
        self.session.add(new_user)
        self.session.commit()
        return User(
            username=new_user.username,
            email=new_user.username,
            name=new_user.name,
            scopes=new_user.scopes,
            favorites=new_user.favorites,
        )

    def delete_user(self, db_user):
        self.session.delete(db_user)
        self.session.commit()
        return User(
            username=db_user.username,
            email=db_user.username,
            name=db_user.name,
            scopes=db_user.scopes,
        )

    def update_user(self, db_user, email=None, name=None, password=None, scopes=None, favorites=None):
        if email:
            db_user.username = email
        if name:
            db_user.name = name
        if scopes:
            db_user.scopes = scopes
        if password:
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode(), salt)
            db_user.password = hashed_password.decode("utf8")
        if favorites:
            db_user.favorites = favorites
        self.session.commit()
        return User(
            username=db_user.username,
            email=db_user.username,
            name=db_user.name,
            scopes=db_user.scopes,
            favorites=db_user.favorites,
        )


backend = BasicBackend()

security = HTTPBasic()


def read_write_auth(username, password) -> User:
    needed_scopes = TOKEN_SCOPES["write"]
    return get_user(username, password, needed_scopes)


def get_user(username, password, needed_scopes) -> User:
    user = backend.get_user(username, password)

    token_scopes = user.scopes

    for scope in needed_scopes.scopes:
        if scope not in token_scopes:
            raise HTTPException(
                status_code=401,
                detail="Insufficient permissions for this action. "
                "Required Scopes: %s Found Scopes: %s" % (needed_scopes.scopes, token_scopes),
            )

    return user


# This is the function that API calls should use as a Depends to ensure
# that they get back the current User from the Authorization header
def auth_check(
    needed_scopes: SecurityScopes, credentials: HTTPBasicCredentials = Depends(security)
):
    return get_user(credentials.username, credentials.password, needed_scopes)


def optional_auth_check(
    username,
    password,
    needed_scopes: SecurityScopes = [TOKEN_SCOPES["read"]],
) -> User | None:
    if username and password:
        return get_user(username, password, needed_scopes)
    return None
