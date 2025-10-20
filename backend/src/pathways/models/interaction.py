from typing import TYPE_CHECKING, List, Optional
import pydgraph

from pydantic import BaseModel

if TYPE_CHECKING:
    from pathways.models.molecule import Molecule
    from pathways.models.protein import Protein


class Interaction(BaseModel):
    name: str
    actor: List["Protein"]
    catalyst: List["Molecule"]
    input: List["Molecule"]
    output: List["Molecule"]
    previous_interaction: Optional["Interaction"] = None
    next_interaction: Optional["Interaction"] = None


def initialize_schema(client: pydgraph.DgraphClient):
    schema = """
    actor: [uid] @reverse .
    catalyst: [uid] @reverse .
    input: [uid] @reverse .
    output: [uid] @reverse .
    previous_interaction: [uid] @reverse .
    next_interaction: [uid] @reverse .

    type Interaction {
        name
        pathway
        actor
        catalyst
        input
        output
        previous_interaction
        next_interaction
    }
    """
    operation = pydgraph.Operation(schema=schema, run_in_background=True)
    return client.alter(operation)
