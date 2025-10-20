import logging
import pydgraph

from pathways.models import base, category, interaction, molecule, pathway, protein
from pathways.settings import Settings


def prepare_seed_database():
    settings = Settings()
    client = get_graphdb_client()
    init_models(client)
    seed_junk_data(client)


def get_graphdb_client() -> pydgraph.DgraphClient:
    settings = Settings()
    connection_string = settings.get_graphdb_url()
    client = pydgraph.open(connection_string)
    return client


def init_models(client: pydgraph.DgraphClient):
    base.initialize_schema(client)
    category.initialize_schema(client)
    interaction.initialize_schema(client)
    molecule.initialize_schema(client)
    pathway.initialize_schema(client)
    protein.initialize_schema(client)


def seed_junk_data(client: pydgraph.DgraphClient):
    """
    Query to test output: 
        query get_interactions_for_pathway ($pathway : string = "Glycolysis")
        {
        interactionList(func: type(Pathway)) @filter(eq(name, $pathway)) {
            uid
            name
            interaction {
                    name
                    input {
                        uid
                        name
                    }
                    output {
                        uid
                        name
                    }
                }
            }
        }
    """
    transaction = client.txn()
    try:
        insert_data = {
            "uid": "_:glycolysis",
            "name": "Glycolysis",
            "dgraph.type": "Pathway",
            "category": [
                {
                    "uid": "_:metabolic",
                    "dgraph.type": "Category",
                }
            ],
            "interaction": [
                {
                    "uid": "_:glycolysis_preparatory_phase",
                    "dgraph.type": "Interaction",
                    "name": "Glycolysis Preparatory Phase",
                    "input": [
                        {
                            "uid": "_:glucose",
                            "dragph.type": "Molecule",
                            "name": "Glucose",
                        },
                        {
                            "uid": "_:atp",
                            "dgraph.type": "Molecule",
                            "name": "ATP",
                        }
                    ],
                    "output": [
                        {
                            "uid": "_:adp",
                            "dgraph.type": "Molecule",
                            "name": "ADP",
                        },
                        {
                            "uid": "_:glucose_6-phosphate",
                            "dgraph.type": "Molecule",
                            "name": "Glucose 6-phosphate",
                        }
                    ],
                    "actor": [
                        {
                            "uid": "_:hexokinase",
                            "dgraph.type": "Protein",
                            "name": "Hexokinase"
                        }
                    ]
                }
            ]
        }
        response = transaction.mutate(set_obj=insert_data)
        # wtf is this? it's unused in example
        print(response)
        commit_response = transaction.commit()
        print(commit_response)
        print(
            'Created pathway named "Glycolysis" with uid = {}'.format(response.uids["glycolysis"])
        )
    except Exception:
        logging.exception("dafuq")
    finally:
        # Clean up. Calling this after txn.commit() is a no-op and hence safe.
        transaction.discard()
