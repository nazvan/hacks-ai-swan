from typing import List, Optional

from fastapi import APIRouter, Depends, Response

from db.dals.session_dal import SessionDAL
from db.schemas.session_schema import SessionCreateSchema, SessionSchema, SessionFullSchema
from dependencies import get_session_dal

router = APIRouter(
    prefix="/session",
    tags=["Session"],
    
)


@router.post("/")
async def create_session(session: SessionCreateSchema, session_dal: SessionDAL = Depends(get_session_dal)):
    return await session_dal.create_session(session)


@router.put("/{session_id}")
async def update_session(session_id: int, name: Optional[str] = None, description: Optional[str] = None,
                      session_dal: SessionDAL = Depends(get_session_dal)):
    return await session_dal.update_session(session_id, name, description)


@router.get("/")
async def get_all_sessions(session_dal: SessionDAL = Depends(get_session_dal)) -> List[SessionSchema]:
    return await session_dal.get_all_sessions()

@router.get("/{session_id}")
async def get_all_sessions(res: Response, session_id: int, session_dal: SessionDAL = Depends(get_session_dal)) -> Optional[SessionFullSchema]:
    session = await session_dal.get_session(session_id)
    if session == None:
        res.status_code = 400
    return  session