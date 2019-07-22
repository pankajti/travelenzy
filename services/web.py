from database.dao.generic_dao import GenericDao
from database.dao.locations_dao import LocationsDao

from database.schema.location import location

g_dao=GenericDao()
l_dao=LocationsDao()

def get_all_locations():
    all_locations = g_dao.get_all_records(location)
    records= [ rec.name for rec in all_locations[0:10]]
    return records