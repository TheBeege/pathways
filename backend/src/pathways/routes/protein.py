from typing import List
from fastapi import APIRouter
from pathways.schemas.protein import ProteinDetail, ProteinListItem

router = APIRouter(
    prefix="/proteins",
    tags=["proteins"],
)

@router.get("/")
async def get_proteins() -> List[ProteinListItem]:
    return [ProteinListItem(
        id="0xa",
        name="bogus",
        interaction=["blarg"],
    )]

@router.get("/{id}")
async def get_protein_detail(id: str) -> ProteinDetail:
    return ProteinDetail(
        id=id,
        name="bogus",
        interaction=["blarg"],
    )
