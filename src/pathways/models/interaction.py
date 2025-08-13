import pydgraph

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
    return client.alter(pydgraph.Operation(schema=schema))