import logging
import pydgraph

from pathways.models import base, category, interaction, molecule, pathway, protein

def get_graphdb_client():
    client = pydgraph.open('dgraph://graphdb:9080')  # TODO: use config env
    return client

def init_models(client: pydgraph.DgraphClient):
    base.initialize_schema(client)
    category.initialize_schema(client)
    interaction.initialize_schema(client)
    molecule.initialize_schema(client)
    pathway.initialize_schema(client)
    protein.initialize_schema(client)

def seed_junk_data(client: pydgraph.DgraphClient):
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
    except Exception as e:
        logging.exception("dafuq")
    finally:
        # Clean up. Calling this after txn.commit() is a no-op and hence safe.
        transaction.discard()
