from datetime import datetime
import datetime

YEAR = 100
MONTH = 1
DATE = 1
SECONDS = 00

'''
getting the satrt time
'''
def get_calendar_time(hours, minutes):
    return datetime.datetime(YEAR, MONTH, DATE, hours, minutes, SECONDS)
'''
adding the talk duration and making it as start time
'''
def get_start_time(time, minutes):
    SECONDS = 60
    return time + datetime.timedelta(0, minutes*SECONDS)