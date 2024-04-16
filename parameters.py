import datetime as dt

TICKER = "AAPL"
START_DATE = "2023-12-01"
LOOK_UP_DAYS = 15      
TRAINING_RATIO = 0.8    # 0.7 == 70%
SCALE_DATA = True

currentDate = str(dt.datetime.now().date())
currentWeekDate = dt.datetime.now().date().strftime("%A")

# """DEBUG"""

# currentDate = "2024-01-01"
# currentWeekDate = "Monday"