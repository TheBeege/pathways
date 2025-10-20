import pydgraph


def initialize_schema(client: pydgraph.DgraphClient):
    schema = """
    name: string @unique @index(exact) .
    interaction: [uid] @reverse .
    pathway: [uid] @reverse .
    """
    return client.alter(pydgraph.Operation(schema=schema))