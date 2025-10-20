from typing import Optional
from fastapi import APIRouter, Depends, Query
from pathways.schemas.protein import ProteinDetail, ProteinListResponse
from pathways.services.protein import ProteinService

router = APIRouter(
    prefix="/proteins",
    tags=["proteins"],
)

@router.get("/")
def get_proteins(
    name: Optional[str] = None,
    protein_service: ProteinService = Depends(ProteinService),
) -> ProteinListResponse:
    return protein_service.list(name)


@router.get("/{id}")
def get_protein_detail(
    id: str,
    protein_service: ProteinService = Depends(ProteinService),
) -> ProteinDetail:
    return protein_service.get(id)
