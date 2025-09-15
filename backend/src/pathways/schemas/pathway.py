from typing import List
from pydantic import BaseModel, Field


class PathwayListItem(BaseModel):
    id: str = Field(..., example="0x7", description="The identifier for this resource")
    name: str = Field(..., example="Glycolysis", description="A biological pathway")
    category: str = Field(..., example="Metabolic", description="The high level category " \
    "of pathways that this belongs to")  # TODO: fix
    interaction: List[str] = Field(..., example="Don't remember", description="a thing!")  # TODO: fix
