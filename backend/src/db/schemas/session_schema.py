from pydantic import BaseModel
from typing import List, Optional

from db.schemas.image_schema import ImageSchema

class SessionCreateSchema(BaseModel):
    name: str
    desc: str 
    # creation_datetime: Optional[int] = time.time()
    # images: List[ChildSchema] = None

    class Config:
        orm_mode = True 

class SessionSchema(BaseModel):
    id: int
    name: Optional[str]
    desc: Optional[str]
    creation_datetime: Optional[int]
    # images: List[ImageSchema] = None

    class Config:
        orm_mode = True 

class SessionFullSchema(BaseModel):
    id: int
    name: str
    desc: str
    creation_datetime: int
    images: List[ImageSchema] = None

    class Config:
        orm_mode = True 