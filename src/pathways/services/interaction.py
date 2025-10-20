import json
import logging
from typing import Optional
import pydgraph
from fastapi import Depends, HTTPException
from pathways.models.interaction import Interaction
from pathways.graphdb import get_graphdb_client
from pathways.utils.logging import get_logger


class InteractionService:

    def __init__(
        self,
        graphdb_client: pydgraph.DgraphClient = Depends(get_graphdb_client),
        logger: logging.Logger = Depends(get_logger)
    ):
        self.graphdb_client = graphdb_client
        self.logger = logger

    def list(self, name: Optional[str]=None):
        transaction = self.graphdb_client.txn(read_only=True)
        query = """
query list($name: string)
{
  interactionList(func: type(Interaction)) @filter(eq(name, $name)) {
    uid
    name
    actor {
      uid
      name
    }
    catalyst {
      uid
      name
    }
    input {
      uid
      name
    }
    output {
    	uid
    	name
  	}
    previous_interaction {
      uid
      name
    }
    next_interacton {
      uid
      name
    }
  }
}
        """
        parameters = {
            "$name": name if name is not None else ""
        }
        try:
            result_json = transaction.query(query, variables=parameters).json
        except Exception:
            self.logger.exception("Failed to fetch list of interactions")
            raise HTTPException(status_code=500, detail="Failed to fetch list of interactions")
        finally:
            transaction.discard()
        result = json.loads(result_json)
        self.logger.debug("result: %r", result)
        return {
            "results": result["interactionList"],
            "page": 0,  # TODO: fix
            "count_per_page": -1,  # TODO: fix
            "total": len(result["interactionList"]),  # TODO: fix
        }
