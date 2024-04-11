import numpy as np
import sklearn
import joblib
import tensorflow as tf

class Predictor:
    __model__ = None
    __datasetScaler__ = None
    __closeScaler__ = None
    def __init__(self) -> None:
        self.__model__ = tf.keras.models.load_model("LSTM15.h5")
        self.__datasetScaler__ = joblib.load("scaler.save")
        self.__closeScaler__ = joblib.load("closePriceScaler")
        
    def inverser(self, closedata):
        '''closedata: an np.array'''
        # transform the shape of the data
        reshaped_data = closedata.reshape(-1, 1)
        result = self.__closeScaler__.inverse_transform(reshaped_data)
        return result
    
    def predict(self, _xData):
        # reshape _xData
        xdata = np.reshape(_xData, (1, _xData.shape[0], 1))
        
        # Performing Prediction
        result = self.__model__.predict(xdata)
        
        # Reverse to original values
        result = self.inverser(result)
        return result[0][0]