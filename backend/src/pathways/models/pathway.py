from typing import TYPE_CHECKING, List
import pydgraph

from pydantic import BaseModel

if TYPE_CHECKING:
    from pathways.models.category import Category
    from pathways.models.interaction import Interaction


class Pathway(BaseModel):
    name: str
    category: List["Category"]
    interaction: List["Interaction"]


def initialize_schema(client: pydgraph.DgraphClient):
    schema = """
    category: [uid] @reverse .

    type Pathway {
        name
        category
        interaction
    }
    """
    operation = pydgraph.Operation(schema=schema, run_in_background=True)
    return client.alter(operation)
