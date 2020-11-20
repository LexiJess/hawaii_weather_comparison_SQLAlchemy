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

#setting up the JSON for precipitation
prev_year=dt.date(2017,8,23)-dt.timedelta(days=365)
results=session.query(measurement.date, measurement.prcp).filter(measurement.date >= prev_year).all()
df= pd.DataFrame(results, columns = ['date', 'precipitation'])
precip_df=df.sort_values("date")
date=precip_df["date"].tolist()
precip=precip_df["precipitation"].tolist()
date_precip=dict(zip(date,precip))
date_precip_json = json.dumps(date_precip) 
precipitation= date_precip_json

app = Flask(__name__)

#Setting up the JSON for stations
session.query(measurement.station).all()
stations=session.query(measurement.station).all()
stations_json=json.dumps(stations)

#Setting up the JSON for temp observations for previous year
results_tobs=session.query(measurement.date, measurement.tobs).filter(measurement.date >= prev_year).all()
df_tobs= pd.DataFrame(results_tobs, columns = ['date', 'temps'])
df_tobs_sorted=df_tobs.sort_values("date")
df_tobs_sorted_date=df_tobs_sorted["date"].tolist()
df_tobs_sorted_temps=df_tobs_sorted["temps"].tolist()
df_tobs_sorted_date_temps=dict(zip(df_tobs_sorted_date,df_tobs_sorted_temps))
df_tobs_sorted_date_temps
tobs=json.dumps(df_tobs_sorted_date_temps)


@app.route("/")
def home():
    return "You can see all the routes: precipitation, stations, temperature observations, and averages"


@app.route("/api/v1.0/precipitation")
def precip():
    return precipitation


@app.route("/api/v1.0/stations")
def places():
    return stations_json

@app.route("/api/v1.0/tobs")
def observations():
    return tobs

@app.route("/api/v1.0/<start>")  
@app.route("/api/v1.0/<start>/<end>")
def averages(start=None, end=None):
    
    return start


@app.route("/jsonified")
def jsonified():
    return jsonify(hello_dict)


if __name__ == "__main__":
    app.run(debug=True)