import pydgraph


def initialize_schema(client: pydgraph.DgraphClient):
    schema = """
    name: string @unique @index(exact) .
    interaction: [uid] @reverse .
    pathway: [uid] @reverse .
    """
    operation = pydgraph.Operation(schema=schema, run_in_background=True)
    return client.alter(operation)
