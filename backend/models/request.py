from pydantic import BaseModel


class Request(BaseModel):
    user_url: str
