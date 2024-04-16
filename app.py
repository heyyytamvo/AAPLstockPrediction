from dataLoader import dataLoader
from Predictor import Predictor
from flask import Flask, jsonify, render_template
import pandas as pd
import parameters
from apscheduler.schedulers.background import BackgroundScheduler

def ApplePrediction():
    # Your function code here
    _dataLoader = dataLoader()
    _predictor = Predictor()

    x_data = _dataLoader.getScaledCloseData()
    _predictor.predict(x_data)
    
# Create a scheduler
scheduler = BackgroundScheduler()
# Add the scheduled job to the scheduler
scheduler.add_job(ApplePrediction, 'cron', hour=9, minute=30)
# Start the scheduler
scheduler.start()
# Create a Flask app
app = Flask(__name__)
# Global flag variable to track whether the function has already run
global firstRun
firstRun = False

def my_startup_function():
    # Your startup function code here
    # Your function code here
    global firstRun

    
    if firstRun == False:
        
        _dataLoader = dataLoader()
        _predictor = Predictor()

        x_data = _dataLoader.getScaledCloseData()
        _predictor.predict(x_data)
        firstRun = True


@app.route('/home', methods=['GET'])
def home():
    return render_template('/Test/index.html')

# Define a route for the API endpoint
@app.route('/api/apple', methods=['GET'])
def Apple():
    df = pd.read_csv("History.txt")
    currentDate = parameters.currentDate
    currentWeekDate = parameters.currentWeekDate
    data = None
    if currentWeekDate != "Saturday" and currentWeekDate != "Sunday":
        # Define the JSON data to return
        data = {
            'Ticker': 'Apple',
            'Date' : currentDate,
            'Weekdate' : currentDate,
            'Predicted Close Price of Today' : float(df["Predicted Close Price"].values[-1]),
            'message' : 'success'
        }
        
    else:
        data = {
            'Ticker': 'Apple',
            'Date' : currentDate,
            'Weekdate' : currentDate,
            'Predicted Close Price of Next Monday' : float(df["Predicted Close Price"].values[-1]),
            'message' : 'success'
        }
    
    # Convert the data to JSON format and return it
    return jsonify(data)

@app.route('/api/history/apple', methods=['GET'])
def AppleHistory():
    df = pd.read_csv("History.txt")
    
    result = {
        'Ticker': 'Apple',
        'Actual' : list(df["Actual Close Price"].values),
        'Predicted' : list(df["Predicted Close Price"].values),
        'Date': list(df['Date'].values),
        'message' : 'success'
    }
    
    # Convert the data to JSON format and return it
    return jsonify(result)


if __name__ == '__main__':
    my_startup_function()
    app.run(host="0.0.0.0", port=3000,debug=False)