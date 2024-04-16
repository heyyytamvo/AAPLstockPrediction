from dataLoader import dataLoader
from Predictor import Predictor
from flask import Flask, jsonify, render_template
import pandas as pd
import parameters

# Create a Flask app
app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    return render_template('Test/index.html')

# Define a route for the API endpoint
@app.route('/api/apple', methods=['GET'])
def Apple():
    _dataLoader = dataLoader()
    _predictor = Predictor()

    x_data = _dataLoader.getScaledCloseData()
    result = _predictor.predict(x_data)
    
    currentDate = parameters.currentDate
    currentWeekDate = parameters.currentWeekDate
    data = None
    if currentWeekDate != "Saturday" and currentWeekDate != "Sunday":
        # Define the JSON data to return
        data = {
            'Ticker': 'Apple',
            'Date' : currentDate,
            'Weekdate' : currentDate,
            'Predicted Close Price of Today' : str(result)
        }
        
    else:
        data = {
            'Ticker': 'Apple',
            'Date' : currentDate,
            'Weekdate' : currentDate,
            'Predicted Close Price of Next Monday' : str(result)
        }
    
    # Convert the data to JSON format and return it
    return jsonify(data)

@app.route('/api/history/apple', methods=['GET'])
def AppleHistory():
    df = pd.read_csv("History.txt")
    
    result = {
        'Ticker': 'Apple',
        'Actual' : list(df["Actual Close Price"].values),
        'Predicted' : list(df["Predicted Close Price"].values)
    }
    
    # Convert the data to JSON format and return it
    return jsonify(result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000,debug=True)