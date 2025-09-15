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
    operation = pydgraph.Operation(schema=schema, run_in_background=True)
    return client.alter(operation)
