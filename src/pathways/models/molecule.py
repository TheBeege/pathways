import pydgraph

def initialize_schema(client: pydgraph.DgraphClient):
    schema = """
    type Molecule {
        name
        interaction
    }
    """
    return client.alter(pydgraph.Operation(schema=schema))