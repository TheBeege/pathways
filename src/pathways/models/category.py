import pydgraph

def initialize_schema(client: pydgraph.DgraphClient):
    schema = """
    type Category {
        name
        pathway
    }
    """
    return client.alter(pydgraph.Operation(schema=schema))