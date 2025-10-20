from typing import List
from pydantic import BaseModel, Field

from pathways.schemas.base import BaseListResponse


class ProteinListItem(BaseModel):
    uid: str = Field(..., example="0x7", description="The identifier for this resource")
    name: str = Field(..., example="Hexokinase", description="A protein")
    # interaction: List[str] = Field(..., example="Don't remember", description="a thing!")  # TODO: fix


class ProteinListResponse(BaseListResponse):
    results: list[ProteinListItem]


class ProteinDetail(BaseModel):
    uid: str = Field(..., example="0x7", description="The identifier for this resource")
    name: str = Field(..., example="Hexokinase", description="A protein")
    # interaction: List[str] = Field(..., example="Don't remember", description="a thing!")  # TODO: fix
