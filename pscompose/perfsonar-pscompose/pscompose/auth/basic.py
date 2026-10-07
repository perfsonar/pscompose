import bcrypt

from typing import Optional
from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException
from pscompose.settings import TOKEN_SCOPES
from pscompose.models import User, UserTable, engine
from fastapi.security import SecurityScopes


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

    def create_user(self, email, name, password, scopes, favorites=None):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        new_user = UserTable(
            username=email,
            name=name,
            password=hashed_password,
            scopes=scopes,
            favorites=favorites or [],
        )
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

    def update_user(
        self, db_user, email=None, name=None, password=None, scopes=None, favorites=None
    ):
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

# HTTPBasic disabled — authentication is handled entirely by the Apache proxy.
# auth_check is kept as a no-op so existing route signatures don't need changes.
_PROXY_USER = User(
    username="admin",
    email="admin",
    name="Proxy-Authenticated User",
    scopes=[s for s in TOKEN_SCOPES.values()],
    favorites=[],
)


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


# auth_check is a no-op: HTTP proxy handles authentication, so every
# request reaching FastAPI is already authenticated. We return a synthetic
# admin user so existing route Security() dependencies keep working without
# any credential challenge.
def auth_check(needed_scopes: SecurityScopes = None):
    return _PROXY_USER


def optional_auth_check(
    username,
    password,
    needed_scopes: SecurityScopes = [TOKEN_SCOPES["read"]],
) -> Optional[User]:
    if username and password:
        return get_user(username, password, needed_scopes)
    return None
