import yaml
import os
import site

TRAVEL_DB_CONFIG = {}
packages = site.getsitepackages()
print(os.path.dirname(os.path.abspath(__file__)))
try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    user_paths = []

environment = os.environ['env'] if 'env' in os.environ else 'dev'
config_exists = False

for path in user_paths+packages:
    print('looking config in path {} '.format(path))
    config_path = '{}/config/config_{}.yaml'.format(path, environment)
    config_exists = True

    if (os.path.exists(config_path)):
        print('found config file : {}'.format(config_path))
        break
else:
    config_path = '/Users/pankaj/dev/git/smu/database_term2/project/travelenzy/config/config_dev.yaml'

with open(config_path, 'r') as file:
    docs = yaml.load_all(file)
    for doc in docs:
        TRAVEL_DB_CONFIG = doc['TRAVEL_DB_CONFIG']

print(TRAVEL_DB_CONFIG)