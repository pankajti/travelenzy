import pymongo
from config.config import TRAVEL_DB_CONFIG


MONGO_DB_CONFIG = TRAVEL_DB_CONFIG['MONGO_DB_CONFIG']

url = 'mongodb://{host}:{port}/'.format(
    port=MONGO_DB_CONFIG.get('port'),
    host=MONGO_DB_CONFIG.get('host'))

db_name=MONGO_DB_CONFIG.get('db_name')


myclient = pymongo.MongoClient(url)
mydb = myclient[db_name]
print(myclient.list_database_names())
