from pydantic import BaseModel
class BBSInput(BaseModel):
    length: float
    width: float
    spacing: float
    dia: int
class QueryRequest(BaseModel):
    query: str

