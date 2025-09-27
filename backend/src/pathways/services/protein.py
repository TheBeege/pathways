import json
import logging
from typing import Dict, List, Optional
from fastapi import Depends
from pathways.graphdb import get_graphdb_client
from pathways.schemas.protein import ProteinListItem
from pathways.util import setup_logger
import pydgraph


class ProteinService:

    def __init__(
        self,
        logger: logging.Logger = Depends(setup_logger),
        db_client: pydgraph.DgraphClient = Depends(get_graphdb_client)
    ):
        self.logger: logging.Logger = logger
        self.db_client: pydgraph.DgraphClient = db_client

    async def get_protein_list(
            self,
            name: Optional[str] = None
    ) -> List[ProteinListItem]:
        transaction = self.db_client.txn()
        filters = [
            ""
        ]
        try:
            result = transaction.query( # pyright: ignore[reportUnknownMemberType, reportUnknownVariableType]
                query=f"""
query get_proteins ($name : string = "")
{
  proteinList(func: type(Protein)) {
    uid
    name
    interaction {
      name
    }
  }
}
"""),
                variables={
                    "name": name,
                }
            )
        except Exception as e:
            self.logger.exception("Failed to query database for protein list")
            # TODO: Make this exception better
            raise RuntimeError(e, "Failed to query database for protein list")
        finally:
            transaction.discard() # pyright: ignore[reportUnknownMemberType]
        result_text: str = result.json() # pyright: ignore[reportUnknownMemberType]
        data: Dict = json.loads(result_text) # pyright: ignore[reportMissingTypeArgument]
        output = [ProteinListItem(item) for item in data.get("proteinList", [])]
        return output
    