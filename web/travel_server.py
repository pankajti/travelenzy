from flask import Flask
from flask import render_template
import json
from flask import send_from_directory
from services import web
from flask import request
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

@app.route('/details')
def serve_details():
    city=request.args.get('location')
    locations, total_time=web.get_all_location_details(city+' ')
    #return render_template('index.html', name='pankaj', details=details)
    return render_template('attractions.html', city=city , attractions=locations, total_time=total_time)
    #return  json.dumps([location[0] for location in locations])

if __name__=='__main__':
    app.run(port=8080)


