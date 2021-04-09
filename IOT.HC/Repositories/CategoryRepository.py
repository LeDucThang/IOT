from Models import CategoryDAO
from sqlalchemy.orm import sessionmaker

class CategoryRepository:
    def __init__(self, session):
        self.session = session

    def List(self):
        CategoryDAOs = self.session.query(CategoryDAO).all()
        return CategoryDAOs
