from db.config import async_session
from db.dals.session_dal import SessionDAL
from db.dals.image_dal import ImageDAL

async def get_session_dal():
    async with async_session() as session:
        async with session.begin():
            yield SessionDAL(session)


async def get_image_dal():
    async with async_session() as session:
        async with session.begin():
            yield ImageDAL(session)