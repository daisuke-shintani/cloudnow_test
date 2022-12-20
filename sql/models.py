from sqlalchemy import Column, ForeignKey, Integer, String, DateTime

from .database import Base


class Cloud(Base):
    __tablename__ ="cloud"
    cloud_id =Column(Integer, primary_key=True, index=True)
    title =Column(String)
    cloud_service =Column(String)
    user_name =Column(String)
    desc =Column(String)
    