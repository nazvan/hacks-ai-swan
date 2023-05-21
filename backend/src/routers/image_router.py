from typing import List, Optional

from fastapi import APIRouter, Depends, File, UploadFile, Query, Response

from db.dals.image_dal import ImageDAL
from db.schemas.image_schema import ImageSchema
from db.schemas.session_schema import SessionSchema
from dependencies import get_image_dal
import os
import json

router = APIRouter(
    prefix="/image",
    tags=["Image"]
)


@router.post("/upload")
async def upload_image(id: int = Query(...),  images: List[UploadFile] = File(...), image_dal: ImageDAL = Depends(get_image_dal)):
    for image in images:
        await image_dal.save_file(image, session_id=id)
    return {'status':200}


@router.get("/{token}")
async def get_all_sessions(res: Response, token: str, image_dal: ImageDAL = Depends(get_image_dal)):
    path = f'data/info/{token}.json'
    if os.path.isfile(path):
        with open(f'data/info/{token}.json') as f:
            info = json.load(f)
            res.status_code = 200
            return info
    else:
        res.status_code = 400
        return {'status':400}



# @router.put("/{session_id}")
# async def update_session(session_id: int, name: Optional[str] = None, description: Optional[str] = None,
#                       session_dal: SessionDAL = Depends(get_session_dal)):
#     return await session_dal.update_session(session_id, name, description)


# @router.get("/{session_id}")
# async def get_all_sessions(session_dal: SessionDAL = Depends(get_session_dal)):
#     return await session_dal.get_all_sessions()
