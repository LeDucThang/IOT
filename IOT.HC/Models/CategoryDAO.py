# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata
class CategoryDAO(Base):
    __tablename__ = 'Category'

    Id = Column(Integer, primary_key=True)
    Code = Column(Text, nullable=False)
    Name = Column(Text, nullable=False)
    TypeId = Column(Integer, nullable=False)
    IconId = Column(Integer, nullable=False)
