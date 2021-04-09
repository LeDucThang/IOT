# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class DeviceDAO(Base):
    __tablename__ = 'Device'

    Id = Column(Text, primary_key=True)
    RoomId = Column(Text, nullable=False)
    AppKey = Column(Text)
    NetKey = Column(Text)
    DeviceKey = Column(Text)
    StatusId = Column(Integer, nullable=False)
    Owner = Column(Integer, nullable=False)
    CreatedAt = Column(Text, nullable=False)
    UpdatedAt = Column(Text, nullable=False)
    DeletedAt = Column(Text)