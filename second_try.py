
import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
session=Session(engine)

app = Flask(__name__)

hello_dict = {"Hello": "World!"}
#precipitation= precip_json
stations= "places"
observations="temps"


@app.route("/")
def home():
    return "You can see all the routes: precipitation, stations, temperature observations, and averages"


@app.route("/api/v1.0/precipitation")
def precip():
    return precipitation

@app.route("/api/v1.0/stations")
def places():
    return stations

@app.route("/api/v1.0/tobs")
def observations():
    return observations

@app.route("/api/v1.0/<start>")  
@app.route("/api/v1.0/<start>/<end>")
def averages(start=None, end=None):
    
    return start


@app.route("/jsonified")
def jsonified():
    return jsonify(hello_dict)


if __name__ == "__main__":
    app.run(debug=True)