from dataLoader import dataLoader
from Predictor import Predictor

_dataLoader = dataLoader()
_predictor = Predictor()

x_data = _dataLoader.getScaledCloseData()
_predictor.predict(x_data)