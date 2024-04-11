import parameters
import numpy as np
import pandas as pd
import yfinance as yf
import datetime as dt
import joblib
import sklearn
import os

class dataLoader:
    __ticker__ = None
    __startDate__ = None
    __endDate__ = None
    __lookUpDays__ = None
    __stockDataFrame__ = None
    __scaledStockDataFrame__ = None
    __closeOriginal__ = None
    __closeScale__ = None
    
    
    def __init__(self, _ticker=parameters.TICKER, _startDay = parameters.START_DATE, _endDate = parameters.END_DATE, _lookUpDays = parameters.LOOK_UP_DAYS):
        self.__ticker__ = _ticker
        self.__startDate__ = _startDay
        self.__endDate__ = _endDate
        self.__lookUpDays__ = _lookUpDays
        downloadedStockData = yf.download(self.__ticker__, self.__startDate__, self.__endDate__)
        self.__stockDataFrame__ = downloadedStockData.tail(self.__lookUpDays__)
        self.__scaledStockDataFrame__ = self.scaleEntireDataset(self.__stockDataFrame__)
        self.__closeOriginal__ = self.__stockDataFrame__["Close"].values
        self.__closeScale__ = self.__scaledStockDataFrame__["Close"].values
        self.writeData()
        
        
        
    def scaleEntireDataset(self, _stockDataFrame):
        ## Load scaler
        Scaler = joblib.load("scaler.save")
        col_names = _stockDataFrame.columns
        features = _stockDataFrame[col_names]
        features = Scaler.transform(features.values)
        scaledDataFrame = pd.DataFrame(features, columns = col_names)
        scaledDataFrame.index = _stockDataFrame.index
        
        return scaledDataFrame
    
    def getScaledCloseData(self):
        return self.__closeScale__
    
    def writeData(self):
        fileName = "History.txt"
        # Check if the file exists
        if not os.path.exists(fileName):
            # Get real Stock Data
            realStock = self.__stockDataFrame__.copy()
            # Drop some column
            realStock.drop(columns="Open", inplace=True)
            realStock.drop(columns="High", inplace=True)
            realStock.drop(columns="Low", inplace=True)
            realStock.drop(columns="Adj Close", inplace=True)
            realStock.drop(columns="Volume", inplace=True)
            
            # Rename close
            realStock = realStock.rename(columns={"Close": "Actual Close Price"})
            
            realStock["Predicted Close Price"] = np.nan
            realStock.to_csv(fileName, sep=',', index=True)
        