# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class HomeControllerDAO(Base):
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
