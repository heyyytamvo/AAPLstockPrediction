import datetime as dt
import pytz

eastern = pytz.timezone('US/Eastern')
TICKER = "AAPL"
START_DATE = "2023-12-01"
LOOK_UP_DAYS = 15      


currentDateTime = dt.datetime.now(eastern)
currentDate = currentDateTime.strftime("%Y-%m-%d")
currentWeekDate = currentDateTime.strftime("%A")
currentHour = currentDateTime.strftime("%H:%M:%S")
