import pandas as pd
from config.config import TRAVEL_DB_CONFIG
import logging
import matplotlib

city_details = pd.read_csv(TRAVEL_DB_CONFIG['CITY_DETAIL_URL'])
indian_cties = city_details[city_details['country']=='India']

city_count = city_details.groupby('country').count()['city']

logging.info(city_details)