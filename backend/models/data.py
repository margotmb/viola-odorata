from pydantic import BaseModel

class Data(BaseModel):
    user_url: str
    url_identifier: str