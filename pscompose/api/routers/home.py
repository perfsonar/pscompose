from fastapi import APIRouter
from pscompose.backends.postgres import backend

# Setup CRUD endpoints
router = APIRouter(tags=["home"])


@router.get(
    "/api/recently_edited",
    summary="Return first 3 items of most recently edited",
)
def recently_edited():
    rows = backend.get_recently_edited(3)
    return rows


@router.get(
    "/api/favorites",
    summary="Return first 3 items of favorites",
)
def favorites():
    rows = backend.get_favorites(3)
    return rows
