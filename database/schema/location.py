from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,Numeric,Date,ForeignKey , Float
from database.connection.mysql_connection import get_connection
Base=declarative_base()

class location(Base):
    __tablename__='location'
    id=Column(Integer,primary_key=True , autoincrement=True)
    lat = Column(Float(12,20))
    lon = Column(Float(12,20))
    state_id=Column(Integer,ForeignKey('state.id', ondelete='CASCADE'))
    population = Column(Integer)
    name=Column(String(200))

class country(Base):
    __tablename__='country'
    id=Column(Integer,primary_key=True, autoincrement=True)
    name=Column(String(50))

class state(Base):
    __tablename__='state'
    id=Column(Integer,primary_key=True, autoincrement=True)
    country_id=Column(Integer,ForeignKey('country.id', ondelete='CASCADE'))
    name=Column(String(250))


def create_schema():
    Base.metadata.create_all(get_connection())
    print('schema created')

create_schema()