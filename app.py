import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import numpy as np
import pandas as pd
import json

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()
measurement=Base.classes.measurement
station=Base.classes.station
session=Session(engine)
from flask import Flask, jsonify  

prev_year=dt.date(2017,8,23)-dt.timedelta(days=365)
results=session.query(measurement.date, measurement.prcp).filter(measurement.date >= prev_year).all()
df= pd.DataFrame(results, columns = ['date', 'precipitation'])
precip_df=df.sort_values("date")

date=precip_df["date"].tolist()
precip=precip_df["precipitation"].tolist()
date_precip=dict(zip(date,precip))
date_precip_json = json.dumps(date_precip) 

app = Flask(__name__)
precipitation= date_precip_json

session.query(measurement.station).all()
stations=session.query(measurement.station).all()
stations=tuple(stations)


observations="temps"

@app.route("/")
def home():
    return "You can see all the routes: precipitation, stations, temperature observations, and averages"


@app.route("/api/v1.0/precipitation")
def precip():
    return precipitation

#the logic for "stations" is in place. It uses a tuple (line 35). Trying to use it returns the error 
#"TypeError: The view function did not return a valid response tuple. 
# The tuple must have the form (body, status, headers), (body, status), or (body, headers)."
#What do I need to do to get the tuple functioning? Why does it need a form that includes more
#than one element?

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