from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from pathways.schemas.protein import ProteinDetail, ProteinListItem
from pathways.services.protein import ProteinService

router = APIRouter(
    prefix="/proteins",
    tags=["proteins"],
)

@router.get("/")
async def get_proteins(
    name: Optional[str] = Query(),
    protein_service: ProteinService = Depends(ProteinService),
) -> List[ProteinListItem]:
    return await protein_service.get_protein_list(name)
    # return [ProteinListItem(
    #     id="0xa",
    #     name="bogus",
    #     interaction=["blarg"],
    # )]

@router.get("/{id}")
async def get_protein_detail(id: str) -> ProteinDetail:
    return ProteinDetail(
        id=id,
        name="bogus",
        interaction=["blarg"],
    )
