#this is my app.py

from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt


from flask import Flask, jsonify

#Jupyter and VSC can run the same code. So we'll take the code that gives us results from Part 1 in Jupyter, copy and paste into VSC and then run it under the
#route such as @app.route("/"), which will then send it to the website that Flask is creating. It's returning a function under that snippet of code, using the variable that we 
# define under the dependencies that we import. Also, run the code in the terminal section at the bottom of VSC by typing in python app.py because the run button isn't working. 


prev_year=dt.date(2017,8,23)-dt.timedelta(days=365)
results=session.query(measurement.date, measurement.prcp).filter(measurement.date >= prev_year).all()
df= pd.DataFrame(results, columns = ['date', 'precipitation'])
precip_df=df.sort_values("date")
precip_df.to_json(path_or_buf=None, orient=None, date_format=None, double_precision=10, force_ascii=True, date_unit='ms', default_handler=None, lines=False, compression='infer', index=True)
precip_json=precip_df.to_json(path_or_buf=None, orient=None, date_format=None, double_precision=10, force_ascii=True, date_unit='ms', default_handler=None, lines=False, compression='infer', index=True)


app = Flask(__name__)

hello_dict = {"Hello": "World!"}
precipitation= precip_json
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