import operator

from app.conference_track_management.slot import fill_slot
from constants import constants


def process_and_schedule_talks(valid_talks):
    valid_talks = sorted(valid_talks.items(),key=operator.itemgetter(1),reverse=True)
    #while(len(valid_talks)!=0):
    morning_slot = fill_slot(constants.TRACK_START_TIME,constants.MORNING_SLOT_DURATION_MINUTES,valid_talks)