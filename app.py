from dataLoader import dataLoader
from Predictor import Predictor
from flask import Flask, jsonify
import pandas as pd
import parameters
from apscheduler.schedulers.background import BackgroundScheduler
import os
import pytz
import datetime as dt

# Create a Flask app
app = Flask(__name__)
predictedResult = None
def ApplePrediction():
    global predictedResult
    # Your function code here
    _dataLoader = dataLoader()
    _predictor = Predictor()
    
    x_data = _dataLoader.getScaledCloseData()
    predictedResult = _predictor.predict(x_data)

    eastern = pytz.timezone('US/Eastern')
    currentDateTime = dt.datetime.now(eastern)
    parameters.currentDate = currentDateTime.strftime("%Y-%m-%d")
    parameters.currentWeekDate = currentDateTime.strftime("%A")
    parameters.currentHour = currentDateTime.strftime("%H:%M:%S")
    
# Create a scheduler
scheduler = BackgroundScheduler(timezone='US/Eastern')
# Add the scheduled job to the scheduler
scheduler.add_job(ApplePrediction, 'cron', hour=9, minute=45)
# Start the scheduler
scheduler.start()

# Global flag variable to track whether the function has already run
global firstRun
firstRun = False

def my_startup_function():
    # Your startup function code here
    # Your function code here
    global predictedResult
    if os.path.exists("History.txt"):
        return
    global firstRun

    
    if firstRun == False:
        
        _dataLoader = dataLoader()
        _predictor = Predictor()

        x_data = _dataLoader.getScaledCloseData()
        predictedResult = _predictor.predict(x_data)
        firstRun = True
my_startup_function()


# Define a route for the API endpoint
@app.route('/api/apple', methods=['GET'])
def Apple(result=predictedResult):
    result = float(result)
    currentDate = parameters.currentDate
    currentWeekDate = parameters.currentWeekDate
    currentHour = parameters.currentHour
    data = None
    if currentWeekDate != "Saturday" and currentWeekDate != "Sunday":
        # Define the JSON data to return
        data = {
            'Ticker': 'AAPL',
            'Timezone': 'Eastern Time (ET)',
            'LastTimeUpdated' : currentHour + ' ' + currentDate + ' EST',
            'Predicted Close Price of Today' : result,
            'message' : 'success',
            'Github Repo' : 'https://github.com/heyyytamvo/AAPLstockPrediction'
        }
        
    else:
        data = {
            'Ticker': 'AAPL',
	    'Timezone': 'Eastern Time (ET)',
            'LastTimeUpdated' : currentHour + ' ' + currentDate + ' EST',
            'Predicted Close Price of Next Monday' : result,
            'message' : 'success',
            'Github Repo' : 'https://github.com/heyyytamvo/AAPLstockPrediction'
        }
    
    # Convert the data to JSON format and return it
    return jsonify(data)

@app.route('/api/history/apple', methods=['GET'])
def AppleHistory():
    df = pd.read_csv("History.txt")
    currentDate = parameters.currentDate
    currentHour = parameters.currentHour
    result = {
        'Ticker': 'AAPL',
        'Timezone': 'Eastern Time (ET)',
	'LastUpdate' : currentHour + ' ' + currentDate + ' EST',
        'Actual' : list(df["Actual Close Price"].values),
        'Predicted' : list(df["Predicted Close Price"].values),
        'Date': list(df['Date'].values),
        'message' : 'success',
        'Github Repo' : 'https://github.com/heyyytamvo/AAPLstockPrediction'
    }
    
    # Convert the data to JSON format and return it
    return jsonify(result)
