import logging
import pymysql

pymysql.install_as_MySQLdb()
import MySQLdb

connection = MySQLdb.Connection(host='localhost', user='travellar', passwd='travellar', db='travelenzy')
cursor = connection.cursor()
logging.warning("Connection with DB established")