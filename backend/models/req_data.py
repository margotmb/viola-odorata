from pydantic import BaseModel


class ReqData(BaseModel):
    user_url: str
