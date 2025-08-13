import pydgraph

def initialize_schema(client: pydgraph.DgraphClient):
    schema = """
    type Protein {
        name
        interaction
    }
    """
    return client.alter(pydgraph.Operation(schema=schema))