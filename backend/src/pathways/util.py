import json
import logging


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