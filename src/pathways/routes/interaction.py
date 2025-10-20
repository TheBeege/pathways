from typing import Optional
from fastapi import APIRouter, Depends, Query

from pathways.schemas.interaction import InteractionCreateRequest, InteractionDetailResponse, InteractionListResponse
from pathways.services.interaction import InteractionService


router = APIRouter(tags=["interactions"])


@router.get("/")  # GET /interactions/
async def list(
    interaction_service: InteractionService = Depends(InteractionService),
    name: Optional[str] = None
) -> InteractionListResponse:
    return interaction_service.list(name)


@router.post("/")  # POST /interactions/
async def create(
    new_interaction_data: InteractionCreateRequest,
    interaction_service: InteractionService = Depends(InteractionService)
) -> InteractionDetailResponse:
    return await interaction_service.create(new_interaction_data)


@router.get("/{id}")  # GET  /interactions/{id}
async def get_detail(
    id: int,
    interaction_service: InteractionService = Depends(InteractionService)
) -> InteractionDetailResponse:
    return await interaction_service.get(id)