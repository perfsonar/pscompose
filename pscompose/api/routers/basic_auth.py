from fastapi import APIRouter, HTTPException, Security
from fastapi_versioning import version
from pscompose.auth import auth_check
from pscompose.settings import TOKEN_SCOPES
from pscompose.auth.basic import backend
from pscompose.models import User, UserCreate, UserUpdate, PasswordReset

router = APIRouter(tags=["HTTP Basic Auth User Management"])


@router.get("/user", summary="List HTTP Basic Auth Users")
@version(1)
def list_users(user: User = Security(auth_check, scopes=[TOKEN_SCOPES["admin"]]), limit=10):
    rows = backend.query(limit=limit)
    return [
        User(username=row.username, email=row.username, name=row.name, scopes=row.scopes)
        for row in rows
    ]


@router.get("/current_user", summary="Return the current HTTP Basic User")
@version(1)
def current_user(user: User = Security(auth_check, scopes=[TOKEN_SCOPES["admin"]])):
    return user


@router.post("/user", summary="Create HTTP Basic Auth User")
@version(1)
def create_user(
    new_user: UserCreate,
    user: User = Security(auth_check, scopes=[TOKEN_SCOPES["admin"]]),
):
    response = backend.create_user(
        email=new_user.username,
        name=new_user.name,
        password=new_user.password,
        scopes=new_user.scopes,
    )
    return response


@router.put("/user/{username}", summary="Update HTTP Basic Auth User")
@version(1)
def update_user(
    username: str,
    update_user: UserUpdate,
    user: User = Security(auth_check, scopes=[TOKEN_SCOPES["admin"]]),
):
    try:
        db_user = backend.query(username=username)[0]
    except Exception:
        raise HTTPException(422)
    response = backend.update_user(
        db_user,
        email=update_user.username,
        name=update_user.name,
        scopes=update_user.scopes,
        password=None,
    )
    return response


@router.delete("/user/{username}", summary="Delete HTTP Basic Auth User")
@version(1)
def delete_user(
    username: str,
    user: User = Security(auth_check, scopes=[TOKEN_SCOPES["admin"]]),
):
    try:
        db_user = backend.query(username=username)[0]
    except Exception:
        raise HTTPException(422)
    response = backend.delete_user(db_user)
    return response


@router.put("/user/{username}/set_password", summary="Set HTTP Basic Auth User Password")
@version(1)
def set_password(
    username: str,
    password: PasswordReset,
    user: User = Security(auth_check, scopes=[TOKEN_SCOPES["admin"]]),
):
    try:
        db_user = backend.query(username=username)[0]
    except Exception:
        raise HTTPException(422)
    response = backend.update_user(db_user, password=password.password)
    return response
