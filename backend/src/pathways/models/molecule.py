from typing import TYPE_CHECKING, List
import pydgraph

from pydantic import BaseModel

if TYPE_CHECKING:
    from pathways.models.interaction import Interaction


class Molecule(BaseModel):
    name: str
    interaction: List["Interaction"]


def initialize_schema(client: pydgraph.DgraphClient):
    schema = """
    type Molecule {
        name
        interaction
    }
    """
    operation = pydgraph.Operation(schema=schema, run_in_background=True)
    return client.alter(operation)
