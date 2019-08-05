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


@app.route('/re')
def serve_react():
    return '{"resp":"hello react"}'

@app.route('/index')
def serve_index():
    locations=web.get_all_locations()
    return render_template('index.html', name='pankaj', locations=locations)

@app.route('/film/<id>')
def serve_film(id = id):
    film = demo_service.get_film(int(id))
    #return render_template('film_detail.html', name='pankaj', film=film, film2 = json.dumps(film) , conv = json2html.convert)
    return json2html.convert(json = film)

    #return json2html.convert(json = json.dumps(film))



@app.route('/location/<id>')
def serve_details(id = id):
    print('found request for {}'.format(id))
    city=request.args.get('location')
    location= location_service.get_location(4)
    #return render_template('index.html', name='pankaj', details=details)
    return render_template('location_detail.html')
    #return  json.dumps([location[0] for location in locations])

if __name__=='__main__':
    app.run(port=8080)