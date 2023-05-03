import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(200), nullable=False)
    password = Column(String(200),  nullable=False)


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    eye_color = Column(String, nullable=False)
    gender = Column(String, nullable=False)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rotation_period = Column(Integer, nullable=False)


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    people_id = Column(Integer, ForeignKey('people.id'))


    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
