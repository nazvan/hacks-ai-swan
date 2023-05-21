from pydantic import BaseModel
import time
from typing import Optional, List
from uuid import uuid4


class ImageSchema(BaseModel):
    session_id: int
    name: Optional[str]
    creation_datetime: Optional[int] = time.time()
    token: str = uuid4()
    classes: str = 'shipun,perdun'

    class Config:
        orm_mode = True 

