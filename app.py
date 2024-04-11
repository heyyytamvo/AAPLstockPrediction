from dataLoader import dataLoader
from Predictor import Predictor

_dataLoader = dataLoader()
_predictor = Predictor()

data = _dataLoader.getScaledCloseData()
predictResult = _predictor.predict(data)
print(predictResult)
