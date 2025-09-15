import json
import logging
from pathways.graphdb import get_graphdb_client, init_models, is_seeded, seed_junk_data
from pathways.routes.pathway import router as pathway_router
from pathways.routes.protein import router as protein_router
import uvicorn
from fastapi import FastAPI


app = FastAPI()

def setup_logger():
    logger = logging.getLogger("pathways")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(json.dumps({
        "time": "%(asctime)s",
        "timestamp": "%(created)f",
        "levelName": "%(levelname)s",
        "functionName": "%(funcName)s",
        "lineNumber": "%(lineno)s",
        "module": "%(module)s",
        "message": "%(message)s",
    }))
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def init():
    setup_logger()
    logger = logging.getLogger("pathways")
    logger.info("Hello from pathways!")
    client = get_graphdb_client()
    logger.debug("got graphdb client")
    if not is_seeded(client):
        logger.info("Data already exists. Not seeding junk data.")
        init_models(client)
        logger.debug("init models done")
        seed_junk_data(client)
        logger.debug("seeding junk data done")

    app.include_router(pathway_router)
    app.include_router(protein_router)


def main():
    init()
    uvicorn.run("pathways.main:app", host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
