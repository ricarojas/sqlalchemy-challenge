from flask import Flask, render_template, request, url_for, redirect
import pymongo
import plotly as plt
import plotly.express as px
from flask.json import jsonify
import pandas as pd
import json

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, MetaData
from sqlalchemy.orm import create_session

# Setup the connection to sqllite & map the tables.

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(autoload_with=engine)
Station = Base.classes.station
Measurement = Base.classes.measurement
session = create_session(bind = engine)

app = Flask(__name__)



@app.route("/")
def home():
    return (
        f"<p>Welcome to the Hawaii weather API!</p>"
        f"<p>Usage:</p>"
        f"/api/v1.0/precipitation<br/>Returns a JSON list of percipitation data for the dates between 8/23/16 and 8/23/17<br/><br/>"
        f"/api/v1.0/stations<br/>Returns a JSON list of the weather stations<br/><br/>"
        f"/api/v1.0/tobs<br/>Returns a JSON list of the Temperature Observations (tobs) for each station for the dates between 8/23/16 and 8/23/17<br/><br/>"
        f"/api/v1.0/start_date<br/>Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for the dates between the given start date and 8/23/17<br/><br/>."
        f"/api/v1.0/start_date/end_date<br/>Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for the dates between the given start date and end date<br/><br/>."
    )

@app.route("/api/v1.0/precipitation")
def percipitation():
   return 'Percipitation'

@app.route("/api/v1.0/stations")
def stations():
    return 'Stations'

@app.route("/api/v1.0/tobs")
def tobs():
    return 'TOBS'

@app.route("/api/v1.0/<start>")
def startdate():
    return 'startdate average min max'

@app.route("/api/v1.0/<start>/<end>")
def startenddate():
    return 'startdate & enddate average min max'