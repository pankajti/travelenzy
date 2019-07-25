from database.connection.mongodb_connection import get_client , get_db

db = get_db('sakila')


def get_film(id ):
    film_detail = db.film.find_one({'film_id': id})
    return film_detail
