from database.connection.mongodb_connection import get_db

db= get_db('films')

print(db)