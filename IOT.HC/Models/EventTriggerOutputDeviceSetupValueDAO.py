# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class EventTriggerOutputDeviceSetupValueDAO(Base):
    __tablename__ = 'EventTriggerOutputDeviceSetupValue'

    EventTriggerId = Column(Text, primary_key=True, nullable=False)
    OutputDeviceId = Column(Text, primary_key=True, nullable=False)
    DeviceAttributeId = Column(Integer, primary_key=True, nullable=False)
    DeviceAttributeValue = Column(Integer)