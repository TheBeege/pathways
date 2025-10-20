from fastapi import Query
from pydantic import BaseModel


class BaseListResponse(BaseModel):
    results: list
    page: int
    count_per_page: int
    total: int


class BasePaginationRequest(BaseModel):
    # Can't get a page below 0
    page: int = Query(ge=0, default=0)
    # Let's not allow more than 200 results per page
    count_per_page: int = Query(ge=1, le=200, default=20)
