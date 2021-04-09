# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class EventTriggerOutputDeviceMappingDAO(Base):
    __tablename__ = 'EventTriggerOutputDeviceMapping'

    EvenTriggerId = Column(Text, primary_key=True, nullable=False)
    OutputDeviceId = Column(Text, primary_key=True, nullable=False)
