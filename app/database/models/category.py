from sqlalchemy import Column,Integer, String
from app.database.base import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String, unique=True)
    description = Column(String,nullable=True)