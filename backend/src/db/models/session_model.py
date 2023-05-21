from sqlalchemy import Column, Integer, String, TIMESTAMP
from db.config import Base


from datetime import datetime
import time
from typing import List, Optional
from sqlalchemy.orm import relationship
from db.schemas.session_schema import SessionCreateSchema



class Session(Base):
    __tablename__ = 'session'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True) #Название сессии
    desc = Column(String, nullable=True) #Описание сессии
    creation_datetime = Column(Integer, nullable=False) #Время создания сессии

    images = relationship("Image", back_populates="session")

    def create(self, session: SessionCreateSchema):
        self.name = session.name
        self.desc = session.desc
        self.creation_datetime = time.time()