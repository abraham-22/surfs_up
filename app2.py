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
    #1. Areate a function welcome() with a return statement.
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


