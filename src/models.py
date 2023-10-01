import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), primary_key=True)


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, primary_key=True)
    mass = Column(Integer, primary_key=True)
    skin_color = Column(String(50), nullable=False)
    hair_color = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    birth_year = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    created = Column(DateTime, nullable=False)
    edited = Column(DateTime, nullable=False)
    homeworld = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)



class FavCharacter(Base):
    __tablename__ = 'favcharacter'
    id = Column(Integer, primary_key=True)
    id_character = Column(Integer, ForeignKey('character.id_character'))
    character = relationship(Character)
    iduser = Column(Integer, ForeignKey('user.iduser'))
    user = relationship(User)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(String(50), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    surface_water = Column(Integer, nullable=False)
    created = Column(DateTime, nullable=False)
    edited = Column(DateTime, nullable=False)
    url = Column(String(50), nullable=False)



class FavPlanets(Base):
    __tablename__ = 'favplanets'
    id = Column(Integer, primary_key=True)
    idplanets = Column(Integer, ForeignKey('planets.id_planets'))
    planets = relationship(Planets)
    iduser = Column(Integer, ForeignKey('user.iduser'))
    user = relationship(User)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
