import pydgraph

def initialize_schema(client: pydgraph.DgraphClient):
    schema = """
    category: [uid] @reverse .

    type Pathway {
        name
        category
        interaction
    }
    """
    return client.alter(pydgraph.Operation(schema=schema))