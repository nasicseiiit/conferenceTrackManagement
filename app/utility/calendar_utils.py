from datetime import datetime, date, time, timedelta
import datetime

'''
getting the satrt time
'''
def get_calendar_time(hours,minutes):
    return datetime.datetime(100,1,1,hours,minutes,00)
'''
adding the talk duration and making it as start time
'''
def get_start_time(time,minutes):
    return time + datetime.timedelta(0, minutes*60)