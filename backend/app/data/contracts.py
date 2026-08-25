from pydantic import BaseModel


class DatasetInfo(BaseModel):
    name: str
    source: str
    description: str
    license: str
