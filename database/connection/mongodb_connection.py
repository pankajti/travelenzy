import pymongo
from config.config import TRAVEL_DB_CONFIG


MONGO_DB_CONFIG = TRAVEL_DB_CONFIG['MONGO_DB_CONFIG']

url = 'mongodb://{host}:{port}/'.format(
    port=MONGO_DB_CONFIG.get('port'),
    host=MONGO_DB_CONFIG.get('host'))

db_name=MONGO_DB_CONFIG.get('db_name')
myclient = pymongo.MongoClient(url)
mydb = myclient[db_name]

def get_client():
    return  myclient

def get_db(db_name):
    mydb = myclient[db_name]
    return mydb


print(myclient.list_database_names())
http://mattturck.com/wp-content/uploads/2019/07/2019_Matt_Turck_Big_Data_Landscape_Final_Fullsize.png