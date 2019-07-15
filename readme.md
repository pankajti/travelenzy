## Objective :

We are using mysql and mongodb to store records related to travel information of a particular city.

## Architecture Diagram


![arch](/Users/pankaj/dev/git/smu/database_term2/project/travelenzy/presentation/travelenzy_Arch.png)


## Setup Steps :

### Install python , Anaconda , MongoDB and Mysql as per the instructions on respective sites.

### Python Setup

#### install python packages

* pip install -r requirements.txt

### DB Setup

* run database\design\setup.sql to create db schema
* run database\schema\create_schema.py to setup schema.

### Setup database collection process

* run data_collection\collect_data.py to collect data from local and web to populate DB tables.

### Run web Server

* run web\travel_server.py to start flask server.

### Client Application

* To be implemented


##  References :


* https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/
* https://stackoverflow.com/questions/53067673/mysql-and-django-on-mac-libssl-1-0-0-dylib-not-loaded
* https://simplemaps.com/data/world-cities