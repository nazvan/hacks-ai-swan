import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from db.schemas.session_schema import SessionSchema

app = FastAPI()

from db.config import engine, Base
from routers import session_router, image_router

app = FastAPI()
app.include_router(session_router.router)
app.include_router(image_router.router)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/images", StaticFiles(directory="./data/images/"), name="images")

@app.on_event("startup")
async def startup():
    # create db tables
    # pass
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == '__main__':
    uvicorn.run("app:app", host='127.0.0.1')
