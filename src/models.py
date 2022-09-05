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
    name = Column(String(40), nullable=False) #The name of this person.
    birth_year  = Column(Integer, nullable=False) #The birth year of the person.
    eye_color  = Column(String(20), nullable=False) #The eye color of this person.
    gender  = Column(String(20), nullable=False) #The gender of this person.
    hair_color  = Column(String(20), nullable=False) #The hair color of this person.
    height  = Column(Integer, nullable=False) #The height of the person in centimeters.
    mass = Column(Integer, nullable=False) #The mass of the person in kilograms.
    skin_color = Column(String(20), nullable=False) #The skin color of this person.
    decription = Column(String(240), nullable=False) #A short description.
    url = Column(String(240), nullable=False) #the hypermedia URL of this resource.
    
class Planet (Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False) #The name of this planet.
    diameter  = Column(Integer, nullable=False) #The diameter of this planet in kilometers.
    rotation_period = Column(Integer, nullable=False) #The number of standard hours it takes for this planet to complete a single rotation on its axis.
    orbital_period = Column(Integer, nullable=False) #The number of standard days it takes for this planet to complete a single orbit of its local star.
    gravity = Column(Integer, nullable=False) # A number denoting the gravity of this planet, where "1" is normal or 1 standard G. "2" is twice or 2 standard Gs. "0.5" is half or 0.5 standard Gs.
    population = Column(Integer, nullable=False) #The average population of sentient beings inhabiting this planet.
    climate = Column(String(40), nullable=False) #The climate of this planet.
    terrain = Column(String(40), nullable=False) #The terrain of this planet.
    surface_water = Column(Integer, nullable=False) # The percentage of the planet surface that is naturally occurring water or bodies of water.
    decription = Column(String(240), nullable=False) #A short description.
    url = Column(String(240), nullable=False) #the hypermedia URL of this resource.

class Starship (Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False) #The name of this starship.
    model  = Column(String(40), nullable=False) #The model or official name of this starship.
    starship_class = Column(String(40), nullable=False) #The class of this starship.
    manufacturer = Column(String(40), nullable=False) #The manufacturer of this starship.
    cost_in_credits = Column(Integer, nullable=False) #The cost of this starship new, in galactic credits.
    length = Column(Integer, nullable=False) #The length of this starship in meters.
    crew  = Column(Integer, nullable=False) # The number of personnel needed to run or pilot this starship.
    passengers  = Column(Integer, nullable=False) #The number of non-essential people this starship can transport.
    max_atmosphering_speed = Column(Integer, nullable=False) #The maximum speed of this starship in the atmosphere.
    hyperdrive_rating = Column(Integer, nullable=False) #The class of this starships hyperdrive.
    cargo_capacity = Column(Integer, nullable=False) #The maximum number of kilograms that this starship can transport.



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
