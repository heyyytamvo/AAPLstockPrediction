import dataLoader
import Predictor

_dataLoader = dataLoader()
_predictor = Predictor()

data = _dataLoader.getScaledCloseData()
predictResult = _predictor.predict(data)
print(predictResult)