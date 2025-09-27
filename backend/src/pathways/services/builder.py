# TODO: Query builder

from enum import Enum


class TargetType(Enum):
    CATEGORY = "Category"
    INTERACTION = "Interaction"
    MOLECULE = "Molecule"
    PATHWAY = "Pathway"
    PROTEIN = "Protein"


class QueryBuilder:
    def __init__(self, output_name: str, target_type: TargetType):
        self.output_name = output_name
        self.target_type = target_type
