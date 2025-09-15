from fastapi import APIRouter
from pathways.schemas.pathway import PathwayListItem

router = APIRouter(
    prefix="/pathways",
    tags=["pathways"],
)

@router.get("/")
async def get_pathways() -> PathwayListItem:
    return PathwayListItem(
        id="0x8",
        name="bogus",
        category="cat",
        interaction=["blarg"],
    )
