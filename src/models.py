import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User (Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), nullable=False)
    email = Column(String(80), nullable=False)
    password = Column(String(20), nullable=False)
    name = Column(String(40))
    last_name = Column(String(40))

class Character (Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    birth_year  = Column(Integer, nullable=False)
    eye_color  = Column(String(20), nullable=False)
    gender  = Column(String(20), nullable=False)
    hair_color  = Column(String(20), nullable=False)
    height  = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    skin_color = Column(String(20), nullable=False)
    decription = Column(String(240), nullable=False)
    img = Column(String(240), nullable=False)
    
clas

# class Person(Base):
#   __tablename__ = 'person'
#  # Here we define columns for the table person
# # Notice that each column is also a normal Python instance attribute.
#id = Column(Integer, primary_key=True)
#name = Column(String(250), nullable=False)

# class Address(Base):
#   __tablename__ = 'address'
# Here we define columns for the table address.
# Notice that each column is also a normal Python instance attribute.
#    id = Column(Integer, primary_key=True)
#   street_name = Column(String(250))
#  street_number = Column(String(250))
# post_code = Column(String(250), nullable=False)
#person_id = Column(Integer, ForeignKey('person.id'))
#  person = relationship(Person)


def to_dict(self):
    return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
