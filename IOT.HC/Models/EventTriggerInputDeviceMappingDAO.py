# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class EventTriggerInputDeviceMappingDAO(Base):
    __tablename__ = 'EventTriggerInputDeviceMapping'

    EventTriggerId = Column(Text, primary_key=True, nullable=False)
    InputDeviceId = Column(Text, primary_key=True, nullable=False)