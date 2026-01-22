from fastapi import APIRouter, HTTPException, Security
from pscompose.backends.postgres import backend
from fastapi_versioning import version

from pscompose.auth import auth_check
from pscompose.settings import TOKEN_SCOPES
from pscompose.auth.basic import backend as backend_user
from pscompose.models import User

# Setup CRUD endpoints
router = APIRouter(tags=["home"])


@router.get(
    "/recently_edited/",
    summary="Return first 3 items of most recently edited",
)
def recently_edited():
    rows = backend.get_recently_edited(3)
    return rows

@router.get("/favorites/{username}/id/", summary="Get current user's list of favorites ids")
@version(1)
def get_user_favorites_id(
    username: str,
    user: User = Security(auth_check, scopes=[TOKEN_SCOPES["read"]]),
):
    try:
        db_user = backend_user.query(username=username)[0]
    except Exception:
        raise HTTPException(status_code=422)

    favorite_ids = getattr(db_user, "favorites", [])
    return favorite_ids

@router.get("/favorites/{username}/", summary="Get current user's list of favorites objects")
@version(1)
def get_user_favorites(
    username: str,
    user: User = Security(auth_check, scopes=[TOKEN_SCOPES["read"]]),
):
    try:
        db_user = backend_user.query(username=username)[0]
    except Exception:
        raise HTTPException(status_code=422)

    favorite_ids = getattr(db_user, "favorites", [])
    if not favorite_ids:
        return [] 

    favorite_objects = backend.get_results_by_ids(favorite_ids, limit=3)
    return favorite_objects 

@router.get("/favorites/{username}/{item_id}/", summary="Return if item is in user's favorites")
@version(1)
def is_user_favorites(
    username: str,
    item_id: str,
    user: User = Security(auth_check, scopes=[TOKEN_SCOPES["read"]]),
):
    try:
        db_user = backend_user.query(username=username)[0]
    except Exception:
        raise HTTPException(status_code=404, detail="User not found")
    
    current_favorites = getattr(db_user, "favorites", [])

    if backend.get_result_by_id(item_id) is None:
        raise HTTPException(status_code=404, detail="Item not found")

    if item_id not in current_favorites:
        return False

    return True

@router.put("/favorites/{username}/{item_id}/", summary="Adding favorite current user's favorites")
@version(1)
def add_user_favorite(
    username: str,
    item_id: str, 
    user: User = Security(auth_check, scopes=[TOKEN_SCOPES["write"]]),
):
    try:
        db_user = backend_user.query(username=username)[0]
    except Exception:
        raise HTTPException(status_code=404, detail="User not found")
    
    # current_favorites = getattr(db_user, "favorites", [])
    current_favorites = [
        f for f in getattr(db_user, "favorites", []) 
        if f and f != 'null'  # Removes '', None, 'null'
    ]

    if backend.get_result_by_id(item_id) is None:
        raise HTTPException(status_code=404, detail="Item not found")

    if item_id not in current_favorites:
        current_favorites.append(item_id)

    response = backend_user.update_user(
        db_user,
        favorites=current_favorites,
    )
    return response

@router.delete("/favorites/{username}/{item_id}/", summary="Deleting favorite current user's favorites")
@version(1)
def delete_user_favorite(
    username: str,
    item_id: str,
    user: User = Security(auth_check, scopes=[TOKEN_SCOPES["write"]]),
):
    try:
        db_user = backend_user.query(username=username)[0]
    except Exception:
        raise HTTPException(status_code=404, detail="User not found")
    
    current_favorites = getattr(db_user, "favorites", [])

    if backend.get_result_by_id(item_id) is None:
        raise HTTPException(status_code=404, detail="Item not found")

    if item_id in current_favorites:
        current_favorites.remove(item_id)

    response = backend_user.update_user(
        db_user,
        favorites=current_favorites,
    )
    return response