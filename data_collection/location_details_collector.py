import request
import requests
from bs4 import BeautifulSoup
import pandas as pd


class LocationDetailsCollector:

    def collec_details_from_wiki(self, location_name):
        response = requests.get('https://en.wikipedia.org/wiki/{}'.format(location_name))
        soup = BeautifulSoup(response.content)
        soup.find_all('h3')[2].find_next_siblings('p')[3].get_text()
        soup.find_all('h1')
        soup.find_all('h2')[4].get_text()
        soup.find_all('h2')[4].find_all_next('h3')
        soup.find_all('h2')[4].find_all_next('h3')[0].find_all_next('p')[0].get_text()

        print(soup)




details_collector = LocationDetailsCollector()

details_collector.collec_details_from_wiki('Mumbai')