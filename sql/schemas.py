import datetime
from fastapi import FastAPI
from pydantic import BaseModel, Field


class CloudCreate(BaseModel):
    
    title : str
    cloud_service : str
    user_name : str
    desc : str
    
    


class Cloud(CloudCreate):
    cloud_id :int
    

    class Config:
        orm_mode =True