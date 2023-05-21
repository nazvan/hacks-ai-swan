from typing import List, Optional

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session as OrmSession

from db.models.image_model import Image
from fastapi import File
import aiofiles

import uuid, json

from ultralytics import YOLO
# Load a model
head_model = YOLO("ai_models/goose_head.pt") 
goose_model = YOLO("ai_models/goose.pt")
classes = {0:'klikun',1:'shipun',2:'maloy'}
#задеплоить не успевали, извините((((((

class ImageDAL():
    def __init__(self, db_session: OrmSession):
        self.db_session = db_session

    async def save_file(self, image: File(...), session_id:int):
        file_data = {'token':str(uuid.uuid4()),
                      'name':image.filename,
                     'session_id':session_id}
        im_path = f'./data/images/{file_data["token"]}.jpg'
        async with aiofiles.open(im_path, 'wb') as out_file:
            while content := await image.read(1024):
                await out_file.write(content)
        data = self.recognize(im_path, file_data["token"])
        file_data['classes']=data['classes']
        new_image = Image(file_data)
        self.db_session.add(new_image)
        await self.db_session.flush()
        return {'status':200}
    
    def recognize(self, image, token):
        result = goose_model.predict(image)[0]
        data = {'size':result.orig_shape,
                'counts':{0:0,1:0,2:0},
                'classes':[],
                'gooses':[]}
        for (boxes, cls, mask) in zip(result.boxes.xywhn,result.boxes.cls, result.masks):
            cls = cls.cpu().tolist()
            data['gooses'].append({
                'box':boxes.cpu().tolist(),
                'class_id':cls,
                'class_name':classes.get(cls),
                'polygon':mask.xyn[0].tolist(),
            })
            data['counts'][cls]+=1
            data['classes'].append(classes.get(cls))

        with open(f'./data/info/{token}.json', 'w') as out_file:
                  json.dump(data,out_file)
        return data
    
    
    
    #     async def get_all_sessions(self) -> List[Session]:
#         q = await self.db_session.execute(select(Session).order_by(Session.id))
#         return q.scalars().all()

#     async def update_session(self, session_id: int, name: Optional[str], desc: Optional[str]):
#         q = update(Session).where(Session.id == book_id)
#         if name:
#             q = q.values(name=name)
#         if desc:
#             q = q.values(desc=desc)
#         q.execution_options(synchronize_session="fetch")
#         await  self.db_session.execute(q)
