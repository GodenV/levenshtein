from pydantic import BaseModel


class LevenshteinResponse(BaseModel):
    distance: int
