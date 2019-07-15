from database.dao.generic_dao import GenericDao
from database.dao.locations_dao import LocationsDao

from database.schema import location

g_dao=GenericDao()
l_dao=LocationsDao()
def get_all_locations():
    records= [ rec.name for rec in g_dao.get_all_records(location)]
    return records