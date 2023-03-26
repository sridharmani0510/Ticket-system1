import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy import select

from sqlalchemy import Session
from sqlalchemy import declarative_base
from sqlalchemy import relationship

Base = declarative_base()

class User(Base):
    __tablename__='user'
    user_id=Column(Integer,autoincrement=True,primary_key=True)
    username=Column(String,unique=True)
    email=Column(String,unique=True)