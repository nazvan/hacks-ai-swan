from typing import List, Optional

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session as OrmSession, selectinload

from db.models.session_model import Session
from db.schemas.session_schema import SessionCreateSchema, SessionSchema, SessionFullSchema

class SessionDAL():
    def __init__(self, db_session: OrmSession):
        self.db_session = db_session

    async def create_session(self, session: SessionCreateSchema):
        new_session = Session()
        new_session.create(session)
        self.db_session.add(new_session)
        await self.db_session.flush()
        return new_session

    async def get_all_sessions(self)->List[SessionSchema]:
        query = await self.db_session.execute(select(Session).options(selectinload(Session.images)).order_by(Session.id))
        return [SessionSchema.from_orm(d) for d in query.scalars().all()]
    
    async def get_session(self, session_id)->Optional[SessionFullSchema]:
        query = await self.db_session.execute(select(Session).where(Session.id==session_id).options(selectinload(Session.images)))
        data = query.scalars().first()
        print(data.images)
        if data is None:
            return None
        else:
            return SessionFullSchema.from_orm(data)

    async def update_session(self, session_id: int, name: Optional[str], desc: Optional[str]):
        q = update(Session).where(Session.id == book_id)
        if name:
            q = q.values(name=name)
        if desc:
            q = q.values(desc=desc)
        q.execution_options(synchronize_session="fetch")
        await  self.db_session.execute(q)
