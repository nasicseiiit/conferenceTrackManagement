import operator

from app.conference_track_management.slot import fill_slot
from constants import constants


def process_and_schedule_talks(valid_talks):
    valid_talks = sorted(valid_talks.items(),key=operator.itemgetter(1),reverse=True)
    morning_slot = fill_slot(constants.MORNING_START_TIME,constants.SLOT_DURATION,valid_talks)