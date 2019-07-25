from database.connection.mongodb_connection import get_client , get_db

db = get_db('sakila')

film_detail = db.film.find({'film_id':1})

for detail in film_detail:
    print(detail)

print(film_detail)

