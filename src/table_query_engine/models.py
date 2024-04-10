from pydantic import BaseModel


class QueryInput(BaseModel):
    query: str


class QueryResponse(BaseModel):
    response: str
