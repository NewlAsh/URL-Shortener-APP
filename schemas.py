#main_schemas.py

from pydantic import BaseModel, ConfigDict, Field
import datetime

class base_class(BaseModel) :
    pass

class Url(base_class):

    url: str = Field(min_length=1)
    expires_at: datetime.datetime | None = None

class Url_Response(base_class):
    model_config = ConfigDict(from_attributes=True)
    url: str
    code_used: str
    expires_at: datetime.datetime | None = None
