import pydgraph

def initialize_schema(client: pydgraph.DgraphClient):
    schema = """
    type Protein {
        name
        interaction
    }
    """
    operation = pydgraph.Operation(schema=schema, run_in_background=True)
    return client.alter(operation)
