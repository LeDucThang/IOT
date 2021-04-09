# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class GroupingDeviceMappingDAO(Base):
    __tablename__ = 'GroupingDeviceMapping'

    GroupingId = Column(Text, primary_key=True, nullable=False)
    DeviceId = Column(Text, primary_key=True, nullable=False)
