from flask import Flask
from flask import render_template
import json
from flask import send_from_directory
from services import web , location_service , demo_service
from flask import request
from json2html import *

from flask_cors import CORS
app= Flask(__name__)

CORS(app)

@app.route('/')
def serve_home():
    return 'Welcome To Travelenzy. Watch this space for updates....'



@app.route('/film/<id>')
def serve_film(id = id):
    film = demo_service.get_film(int(id))
    #return render_template('film_detail.html', name='pankaj', film=film, film2 = json.dumps(film) , conv = json2html.convert)
    return json2html.convert(json = json.dumps(film))




@app.route('/film/<id>')
def serve_location(id = id ):
    film = {'name': 'madhishala'}
    film = location_service.get_location()
    return render_template('film_detail.html', name='pankaj', film=json.dumps(film))



if __name__=='__main__':
    app.run(port=8080)