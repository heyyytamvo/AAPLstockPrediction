import numpy as np
import sklearn
import joblib
import tensorflow as tf
import os
import numpy as np
import datetime as dt
import parameters

class Predictor:
    __model__ = None
    __datasetScaler__ = None
    __closeScaler__ = None
    def __init__(self) -> None:
        self.__model__ = tf.keras.models.load_model("LSTM15.h5")
        self.__datasetScaler__ = joblib.load("scaler.save")
        self.__closeScaler__ = joblib.load("closePriceScaler.save")
        
    def inverser(self, closedata):
        '''closedata: an np.array'''
        # transform the shape of the data
        reshaped_data = closedata.reshape(-1, 1)
        result = self.__closeScaler__.inverse_transform(reshaped_data)
        return result
    
    def writeResult(self, predictedPrice):
        # Get the date and week day
        # day_of_week = str(dt.datetime.now().date().strftime('%A'))
        # currentDate = str(dt.datetime.now().date())
        
        # DEBUG
        day_of_week = parameters.currentWeekDate
        currentDate = parameters.currentDate
        
        if (day_of_week == "Saturday") or (day_of_week == "Sunday"):
            pass
        


        else:
            fileName = "History.txt"
            currentDate = parameters.currentDate
            ## Open History.txt and write new data
            newRecord = f"{currentDate},{-1},{-1}"
            with open(fileName, 'a') as file:
                file.write(newRecord)
            
            with open(fileName, 'r') as file:
                lines = file.readlines()
            

            ### Modify the second column in the last record : Actual Price
            last_record = lines[-1].split(',')

            ## CaseHandle: when worker shutdown and re run
            #if (last_record[1] == '-1'):
            #x    return
            ## Modify the second column in the last record
            last_record = lines[-1].split(',')
            last_record[2] = str(predictedPrice)
            

            ### Construct the modified last record string
            modified_last_record = ','.join(last_record)
            modified_last_record += '\n'
            ### Replace the last record in the lines list
            lines[-1] = modified_last_record

            ### Write the modified lines back to the file
            with open(fileName, 'w') as file:
                file.writelines(lines)
            
    def predict(self, _xData):
        # reshape _xData
        xdata = np.reshape(_xData, (1, _xData.shape[0], 1))
        
        # Performing Prediction
        result = self.__model__.predict(xdata)
        
        # Reverse to original values
        result = self.inverser(result)
        self.writeResult(result[0][0])
        
        return result[0][0]
