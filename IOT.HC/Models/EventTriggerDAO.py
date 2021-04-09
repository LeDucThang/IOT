# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class EventTriggerDAO(Base):
    __tablename__ = 'EventTrigger'

    Id = Column(Text, primary_key=True)
    GroupId = Column(Text, nullable=False)
    EvenTriggerTypeId = Column(Integer, nullable=False)
    Priority = Column(Integer, nullable=False)
    Name = Column(Text, nullable=False)
    HasTimer = Column(Integer, nullable=False)
    StartAt = Column(Integer)
    EndAt = Column(Integer)
    HasRepeater = Column(Integer, nullable=False)
    EachMonday = Column(Integer, nullable=False)
    EachTuesday = Column(Integer, nullable=False)
    EachWednesday = Column(Integer, nullable=False)
    EachThursday = Column(Integer, nullable=False)
    EachFriday = Column(Integer, nullable=False)
    EachSaturday = Column(Integer, nullable=False)
    EachSunday = Column(Integer, nullable=False)
    HasNotification = Column(Integer, nullable=False)
    NotificationDelayTime = Column(Integer, nullable=False)
    LogicalOperatorId = Column(Integer, nullable=False)
    CreatedAt = Column(Integer, nullable=False)
    UpdatedAt = Column(Text, nullable=False)
    DeletedAt = Column(Text)


