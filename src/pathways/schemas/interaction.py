from pydantic import BaseModel

from pathways.schemas.base import BaseListResponse


class InteractionListItem(BaseModel):
    uid: str
    name: str


class InteractionListResponse(BaseListResponse):
    results: list[InteractionListItem]


class InteractionDetailResponse(BaseModel):
    uid: str
    name: str


class InteractionCreateRequest(BaseModel):
    name: str
