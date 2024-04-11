import datetime as dt

TICKER = "AAPL"
START_DATE = "2010-01-01"
END_DATE = str(dt.datetime.now().date())
LOOK_UP_DAYS = 15      
TRAINING_RATIO = 0.8    # 0.7 == 70%
SCALE_DATA = True
