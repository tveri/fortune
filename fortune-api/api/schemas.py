from pydantic import BaseModel


class TunedModel(BaseModel):
    class Config:
        orm_mode = True
    

class ShowUser(TunedModel):
    full_name: str