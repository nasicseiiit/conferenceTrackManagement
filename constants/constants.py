from app.utility import clendar_utils

LUNCH_DURATION_MINUTES = 60
LUNCH_TALK =  "Lunch"
NETWORKING_DURATION_MINUTES = 60

LIGHTNING_DURATION_MINUTES = 5

TOTAL_TRACK_DURATION_MINUTES = 420
MORNING_SLOT_DURATION_MINUTES = 180
AFTERNOON_SLOT_DURATION_MINUTES = 240

TRACK_START_TIME = clendar_utils.get_calendar_time(9, 0)
LUNCH_START_TIME = clendar_utils.get_calendar_time(12, 0)
POST_LUNCH_SLOT_START_TIME = clendar_utils.get_calendar_time(13, 0)
NETWORKING_START_TIME = clendar_utils.get_calendar_time(17, 0)