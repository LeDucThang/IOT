from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .CategoryRepository import CategoryRepository

class UOW:
    def __init__(self):
        engine = create_engine('sqlite:///IOTHC.db')
        engine.connect()
        Session = sessionmaker(bind=engine)
        session = Session()
        self.CategoryRepository = CategoryRepository(session)
