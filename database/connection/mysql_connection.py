import logging
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import TRAVEL_DB_CONFIG


pymysql.install_as_MySQLdb()
import MySQLdb

connection = MySQLdb.Connection(host='localhost', user='travellar', passwd='travellar', db='travelenzy')
cursor = connection.cursor()
logging.warning("Connection with DB established")

url1= 'mysql+pymysql://travellar:travellar@localhost/travelenzy'

engine1 = create_engine(url1, pool_recycle=3600)

MYSQL_DB_CONFIG = TRAVEL_DB_CONFIG['MYSQL_DB_CONFIG']

url = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db_name}'.format(
    username=MYSQL_DB_CONFIG.get('username'),
    password=MYSQL_DB_CONFIG.get('password'),
    port=MYSQL_DB_CONFIG.get('port'),
    host=MYSQL_DB_CONFIG.get('host'),
    db_name=MYSQL_DB_CONFIG.get('db_name')
)

engine=create_engine(url, pool_recycle=3600)

def get_connection():
    return engine.connect()

def get_session():
    Session = sessionmaker(bind=engine)
    return Session()



