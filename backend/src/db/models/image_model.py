from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from db.config import Base


from datetime import datetime
import time
from typing import List, Optional
from sqlalchemy.orm import relationship

from db.models.session_model import Session
from uuid import uuid4


class Image(Base):
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey(Session.id), nullable = False)
    name = Column(String, nullable=False)
    token = Column(String, nullable=False)
    creation_datetime = Column(Integer, nullable=False) #Время создания сессии
    classes = Column(String)

    session = relationship("Session", back_populates="images")

    def __init__(self, data):
        self.token = data.get('token')
        self.session_id = data.get('session_id')
        self.name = data.get('name')
        self.creation_datetime = time.time()
        self.classes = ','.join(data.get('classes'))