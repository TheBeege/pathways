from typing import TYPE_CHECKING, List
import pydgraph
from pydantic import BaseModel

if TYPE_CHECKING:
    from pathways.models.pathway import Pathway


class Category(BaseModel):
    name: str
    pathway: List["Pathway"]


def initialize_schema(client: pydgraph.DgraphClient):
    schema = """
    type Category {
        name
        pathway
    }
    """
    return client.alter(pydgraph.Operation(schema=schema))