import pandas as pd
from config.config import TRAVEL_DB_CONFIG
import logging
from database.schema.location import location, state, country
from database.dao.locations_dao import LocationsDao
from database.dao.generic_dao import GenericDao

import matplotlib

city_details = pd.read_csv(TRAVEL_DB_CONFIG['CITY_DETAIL_URL'])
l_dao= LocationsDao()
g_dao = GenericDao()

for idx , city in city_details.iterrows() :
    loc = location()
    loc.name = city['city']
    loc.lat = city['lat']
    loc.lon = city['lng']
    f_state = city['admin_name'] if not pd.isnull(city['admin_name']) else None
    f_cnt = city['country'] if not pd.isnull(city['country']) else None
    loc.population = None if pd.isnull(city['population']) else city['population']
    cnt = l_dao.find_country_by_name(f_cnt)
    st = l_dao.find_state_by_name(f_state)
    print('  creating for {} {} {}  '.format(loc.name, f_cnt, f_state))


    if cnt is None or len(cnt) ==0    :
        c = country()
        c.name=f_cnt
        g_dao.insert_record(c)
        cnt= [c]

    if st is None or len(st) ==0  :
        s = state()
        s.name=f_state
        s.country_id = cnt[0].id
        g_dao.insert_record(s)
        st = [s]
    loc.state_id = st[0].id
    g_dao.insert_record(loc)

logging.info('all records inserted')



