import json
import logging
from typing import Dict, List, Optional
from fastapi import Depends, HTTPException
from pathways.graphdb import get_graphdb_client
from pathways.schemas.protein import ProteinListItem
from pathways.utils.logging import get_logger
import pydgraph


class ProteinService:

    def __init__(
        self,
        logger: logging.Logger = Depends(get_logger),
        db_client: pydgraph.DgraphClient = Depends(get_graphdb_client)
    ):
        self.logger: logging.Logger = logger
        self.db_client: pydgraph.DgraphClient = db_client

    def list(
        self,
        name: Optional[str] = None
    ) -> List[ProteinListItem]:
        transaction = self.db_client.txn(read_only=True)
        # filters = [""]  # TODO: this
        query = """
query get_proteins ($name: string)
{
    proteinList(func: type(Protein)) @filter(eq(name, $name)) {
        uid
        name
        interaction {
            uid
            name
        }
    }
}
        """
        try:
            result_json = transaction.query(
                query=query,
                variables={
                    "$name": name if name is not None else "",
                }
            ).json
        except Exception as e:
            self.logger.exception("Failed to query database for protein list")
            raise HTTPException(status_code=500, detail="Failed to fetch list of proteins")
        finally:
            transaction.discard()
        result: str = json.loads(result_json)
        self.logger.debug("result: %r", result)
        return {
            "results": result["proteinList"],
            "page": 0,  # TODO: fix
            "count_per_page": -1,  # TODO: fix
            "total": len(result["proteinList"]),  # TODO: fix
        }

    def get(
        self,
        uid: str
    ) -> Dict:
        transaction = self.db_client.txn(read_only=True)
        query = """
query get($uid: string)
{
    protein(func: uid($uid)) {
        uid
        name
        interaction {
            uid
            name
        }
    }
}
        """
        variables = {
            "$uid": uid
        }
        try:
            result_json = transaction.query(
                query=query,
                variables=variables,
            ).json
        except Exception as e:
            self.logger.exception("Failed to query database for protein")
            raise HTTPException(status_code=500, detail="Failed to fetch protein")
        finally:
            transaction.discard()
        result: str = json.loads(result_json)
        self.logger.debug("result: %r", result)
        if len(result["protein"]) == 0:
            raise HTTPException(status_code=404, detail="Failed to find a protein by that ID")
        return result["protein"][0]
