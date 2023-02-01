import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, primary_key=True)
    usuario = Column(String(250), nullable=False)
    contraseña = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person 
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    contents = Column(String(250), nullable=False)
    text = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'))


class Comentarios(Base):
    __tablename__ = 'comentarios'
    # Here we define columns for the table person 
    # Notice that each column is also a normal Python instance attribute.
    comm_id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('user.post_id'))
    user_id = Column(Integer, ForeignKey('user.user_id'))
    
class Seguidor (Base):
    __tablename__ = 'seguidor'
    # Here we define columns for the table person 
    # Notice that each column is also a normal Python instance attribute.
    seguidor_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('user.post_id'))
    from_user_id = Column(Integer, ForeignKey('user.user_id'))
    to_user_id = Column(Integer, ForeignKey('user.user_id'))
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e