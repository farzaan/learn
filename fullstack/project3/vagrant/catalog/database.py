import sys

from sqlalchemy import  Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative  import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

from sqlalchemy import create_engine

Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'

    name = Column(String(80), nullable = False)

    id =  Column(Integer, primary_key = True)

class Item(Base):
    __tablename__ = 'item'

    name = Column(String(80))
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    username = Column(String(50))
    category = relationship(Category)

    @property
    def serialize(self):

        return {
        'name': self.name,
        'description': self.description,
        'username': self.username,
        'id': self.id,
        }

        

engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)



