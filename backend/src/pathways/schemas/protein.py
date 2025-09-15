from typing import List
from pydantic import BaseModel, Field


class ProteinListItem(BaseModel):
    id: str = Field(..., example="0x7", description="The identifier for this resource")
    name: str = Field(..., example="Hexokinase", description="A protein")
    interaction: List[str] = Field(..., example="Don't remember", description="a thing!")  # TODO: fix


class ProteinDetail(BaseModel):
    id: str = Field(..., example="0x7", description="The identifier for this resource")
    name: str = Field(..., example="Hexokinase", description="A protein")
    interaction: List[str] = Field(..., example="Don't remember", description="a thing!")  # TODO: fix
