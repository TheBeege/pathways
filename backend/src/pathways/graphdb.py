import json
import logging
from pathways.config import Settings
import pydgraph

from pathways.models import base, category, interaction, molecule, pathway, protein

def get_graphdb_client() -> pydgraph.DgraphClient:
    settings = Settings()
    client = pydgraph.open(f'dgraph://{settings.db_host}:{settings.db_port}')
    return client

def init_models(client: pydgraph.DgraphClient):
    base.initialize_schema(client)
    category.initialize_schema(client)
    interaction.initialize_schema(client)
    molecule.initialize_schema(client)
    pathway.initialize_schema(client)
    protein.initialize_schema(client)

def seed_junk_data(client: pydgraph.DgraphClient):
    logger = logging.getLogger("pathways")
    logger.info("starting seed junk data...")
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
        logger.debug(response)
        commit_response = transaction.commit()
        logger.debug(commit_response)
        logger.info(
            'Created pathway named "Glycolysis" with uid = {}'.format(response.uids["glycolysis"])
        )
    except Exception as e:
        logger.exception("dafuq")
    finally:
        # Clean up. Calling this after txn.commit() is a no-op and hence safe.
        transaction.discard()


def is_seeded(client: pydgraph.DgraphClient) -> bool:
    logger = logging.getLogger("pathways")
    transaction = client.txn()
    ## Check if data exists already
    query = """
query get_pathway_io_molecules ($pathway : string = "Glycolysis")
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
    result = transaction.query(query)
    
    data = json.loads(result.json)
    logger.debug("data: %r", json.dumps(data))
    has_seed_data = len(data.get("interactionList", [])) != 0
    transaction.discard()
    return has_seed_data
