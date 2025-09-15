import json
import logging
from pathways.graphdb import get_graphdb_client, init_models, is_seeded, seed_junk_data

def main():
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
    logger.info("Hello from pathways!")
    client = get_graphdb_client()
    logger.debug("got graphdb client")
    if not is_seeded(client):
        logger.info("Data already exists. Not seeding junk data.")
        init_models(client)
        logger.debug("init models done")
        seed_junk_data(client)
        logger.debug("seeding junk data done")

if __name__ == "__main__":
    main()
