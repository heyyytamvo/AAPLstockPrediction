import datetime as dt
import pytz


TICKER = "AAPL"
START_DATE = "2023-12-01"
LOOK_UP_DAYS = 15      

global currentDateTime
global currentDate
global currentWeekDate
global currentGlobal

eastern = pytz.timezone('US/Eastern')
currentDateTime = dt.datetime.now(eastern)
currentDate = currentDateTime.strftime("%Y-%m-%d")
currentWeekDate = currentDateTime.strftime("%A")
currentHour = currentDateTime.strftime("%H:%M:%S")
