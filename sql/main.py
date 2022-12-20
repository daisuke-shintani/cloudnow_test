import datetime
from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from . import crud,models,schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app=FastAPI()
origins = [
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 題名
@app.get("/clouds/{search}")
async def search_cloud(search: str, skip: int =0, limit: int =50,  db: Session = Depends(get_db) ):
    title =crud.get_search(search, db, skip=skip, limit=limit)
    return title
# 確認
@app.get("/clouds", response_model=List[schemas.Cloud])
async def read_clouds(skip: int =0, limit: int =50,  db: Session = Depends(get_db)):
    clouds =crud.get_clouds(db, skip=skip, limit=limit)
    return clouds

@app.post("/clouds", response_model=schemas.Cloud)
async def create_cloud(cloud: schemas.CloudCreate, db: Session = Depends(get_db)):
    return crud.create_cloud(db=db, cloud=cloud)