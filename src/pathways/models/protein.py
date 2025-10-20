from typing import TYPE_CHECKING, List
import pydgraph

from pydantic import BaseModel

if TYPE_CHECKING:
    from pathways.models.interaction import Interaction


class Protein(BaseModel):
    name: str
    interaction: List["Interaction"]


def initialize_schema(client: pydgraph.DgraphClient):
    schema = """
    type Protein {
        name
        interaction
    }
    """
    return client.alter(pydgraph.Operation(schema=schema))