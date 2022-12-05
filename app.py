# Set Up the Flask Weather App
import datetime as dt
import numpy as np
import pandas as pd

# Import dependencies we need for SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import the dependencies that we need for Flask.
from flask import Flask, jsonify

# Set Up the Database.
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into our classes and then reflect our tables.
Base = automap_base()
Base.prepare(engine, reflect=True)

# Create a variable for each of the classes.
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database.
session = Session(engine)

# Set Up Flask: create a Flask application called "app."
app = Flask(__name__)

# Define the welcome route- the homepage.
@app.route("/")

# Add the routing information for each of the other routes.
    #1. Create a function welcome() with a return statement.
def welcome():
    return(
    #2. Add the routes that we'll need for this module into our return statement.
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Split up the code to the respective routes.
#1. Build route for the precipitation analysis and create the precipitation() function.
@app.route("/api/v1.0/precipitation")
def precipitation():
    #1.1. Calculates the date one year ago from the most recent date in the db.
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #1.2. Query to get the date and precipitation for the previous year.
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

#2. Build the stations route- begin by defining the route and route name.
@app.route("/api/v1.0/stations")
def stations():
    #2.1. Create a query that will allow us to get all of the stations in our db.
    results = session.query(Station.station).all()
    #2.2. Convert the results to a list.
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

#3. Create the temperature observations route and create a function called temp_monthly().
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #3.1.  Query the primary station for all the temperature observations.
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    #3.2. Convert the results to a list.
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#4. Create a route and function for our summary statistics report.
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
    #4.1.  Add start and end parameters to our stats()function
def stats(start=None, end=None):
    #4.2. Query our database using the sel list.
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)
    
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)


