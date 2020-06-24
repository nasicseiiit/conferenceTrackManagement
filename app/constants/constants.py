from app.utility import calendar_utils

FILE_ERROR = "The input file is not exist"

LUNCH_DURATION_MINUTES = 60
LUNCH_TALK =  "Lunch"
NETWORKING_DURATION_MINUTES = 60
NWTWORKING_EVENT = "Networking Event"

LIGHTNING_DURATION_MINUTES = 5

TOTAL_TRACK_DURATION_MINUTES = 420
MORNING_SLOT_DURATION_MINUTES = 180
AFTERNOON_SLOT_DURATION_MINUTES = 240

TRACK_START_TIME = calendar_utils.get_calendar_time(9, 0)
LUNCH_START_TIME = calendar_utils.get_calendar_time(12, 0)
POST_LUNCH_SLOT_START_TIME = calendar_utils.get_calendar_time(13, 0)
NETWORKING_START_TIME = calendar_utils.get_calendar_time(17, 0)