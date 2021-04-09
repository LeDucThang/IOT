# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Category(Base):
    __tablename__ = 'Category'

    Id = Column(Integer, primary_key=True)
    Code = Column(Text, nullable=False)
    Name = Column(Text, nullable=False)
    TypeId = Column(Integer, nullable=False)
    IconId = Column(Integer, nullable=False)


class CategoryDeviceAttributeMapping(Base):
    __tablename__ = 'CategoryDeviceAttributeMapping'

    CategoryId = Column(Integer, primary_key=True, nullable=False)
    DeviceAttributeId = Column(Integer, primary_key=True, nullable=False)


class ComparisonOperator(Base):
    __tablename__ = 'ComparisonOperator'

    Id = Column(Integer, primary_key=True)
    Code = Column(Text, nullable=False)
    Name = Column(Text, nullable=False)


class Device(Base):
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


class DeviceAttribute(Base):
    __tablename__ = 'DeviceAttribute'

    Id = Column(Integer, primary_key=True)
    Code = Column(Text, nullable=False)
    Name = Column(Text, nullable=False)


class EventTrigger(Base):
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


class EventTriggerInputDeviceMapping(Base):
    __tablename__ = 'EventTriggerInputDeviceMapping'

    EventTriggerId = Column(Text, primary_key=True, nullable=False)
    InputDeviceId = Column(Text, primary_key=True, nullable=False)


class EventTriggerInputDeviceSetupValue(Base):
    __tablename__ = 'EventTriggerInputDeviceSetupValue'

    EventTriggerId = Column(Text, primary_key=True, nullable=False)
    InputDeviceId = Column(Text, primary_key=True, nullable=False)
    DeviceAttributeId = Column(Integer, primary_key=True, nullable=False)
    ComparisonOperatorId = Column(Integer)
    DeviceAttributeValue = Column(Integer)


class EventTriggerOutputDeviceMapping(Base):
    __tablename__ = 'EventTriggerOutputDeviceMapping'

    EvenTriggerId = Column(Text, primary_key=True, nullable=False)
    OutputDeviceId = Column(Text, primary_key=True, nullable=False)


class EventTriggerOutputDeviceSetupValue(Base):
    __tablename__ = 'EventTriggerOutputDeviceSetupValue'

    EventTriggerId = Column(Text, primary_key=True, nullable=False)
    OutputDeviceId = Column(Text, primary_key=True, nullable=False)
    DeviceAttributeId = Column(Integer, primary_key=True, nullable=False)
    DeviceAttributeValue = Column(Integer)


class EventTriggerOutputGroupingMapping(Base):
    __tablename__ = 'EventTriggerOutputGroupingMapping'

    EventTriggerId = Column(Text, primary_key=True, nullable=False)
    OutputGroupingId = Column(Text, primary_key=True, nullable=False)


class EventTriggerOutputGroupingSetupValue(Base):
    __tablename__ = 'EventTriggerOutputGroupingSetupValue'

    EventTriggerId = Column(Text, primary_key=True, nullable=False)
    GroupingId = Column(Text, primary_key=True, nullable=False)
    DeviceAttributeId = Column(Integer, primary_key=True, nullable=False)
    DeviceAttributeValue = Column(Integer)


class EventTriggerOutputSceneMapping(Base):
    __tablename__ = 'EventTriggerOutputSceneMapping'

    EventTriggerId = Column(Text, primary_key=True, nullable=False)
    OutputSceneId = Column(Text, primary_key=True, nullable=False)


class EventTriggerType(Base):
    __tablename__ = 'EventTriggerType'

    Id = Column(Integer, primary_key=True)
    Code = Column(Text, nullable=False)
    Name = Column(Text, nullable=False)


class Grouping(Base):
    __tablename__ = 'Grouping'

    Id = Column(Text, primary_key=True)
    Name = Column(Text, nullable=False)
    CategoryId = Column(Integer)


class GroupingDeviceMapping(Base):
    __tablename__ = 'GroupingDeviceMapping'

    GroupingId = Column(Text, primary_key=True, nullable=False)
    DeviceId = Column(Text, primary_key=True, nullable=False)


class HomeController(Base):
    __tablename__ = 'HomeController'

    Id = Column(Text, primary_key=True)
    Name = Column(Text, nullable=False)
    Mac = Column(Text, nullable=False)
    IpAddress = Column(Text, nullable=False)
    DormitoryId = Column(Text, nullable=False)
    TimeZone = Column(Integer, nullable=False)
    Version = Column(Text, nullable=False)
    VersionUpdatedAt = Column(Text, nullable=False)
    CreatedAt = Column(Integer, nullable=False)
    UpdatedAt = Column(Text, nullable=False)
    DeletedAt = Column(Text)


class DeviceAttributeValue(Base):
    __tablename__ = 'DeviceAttributeValue'

    DeviceId = Column(ForeignKey('Device.Id'), primary_key=True, nullable=False)
    DeviceAttributeId = Column(ForeignKey('DeviceAttribute.Id'), primary_key=True, nullable=False)
    ExpectedValue = Column(Integer)
    RealValue = Column(Integer)

    DeviceAttribute = relationship('DeviceAttribute')
    Device = relationship('Device')
