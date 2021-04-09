# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class GroupingDAO(Base):
    __tablename__ = 'Grouping'

    Id = Column(Text, primary_key=True)
    Name = Column(Text, nullable=False)
    CategoryId = Column(Integer)
