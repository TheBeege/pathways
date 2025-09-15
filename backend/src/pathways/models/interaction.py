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
    operation = pydgraph.Operation(schema=schema, run_in_background=True)
    return client.alter(operation)
