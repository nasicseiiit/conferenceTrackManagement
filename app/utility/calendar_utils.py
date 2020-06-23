from datetime import datetime, date, time, timedelta
import datetime

def get_calendar_time(hours,minutes):
    return datetime.datetime(100,1,1,hours,minutes,00)

def get_start_time(time,minutes):
    return time + datetime.timedelta(0, minutes*60)