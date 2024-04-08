from pydantic import BaseModel, Field
from typing import Dict
from typing_extensions import Annotated

ShortUrl = Annotated[str, Field(ge=0)]


class DataJSON(BaseModel):
    long_url: str
    short_url: str


class DataURLS(BaseModel):
    urls: Dict[str, DataJSON] = Field(default_factory=dict)

