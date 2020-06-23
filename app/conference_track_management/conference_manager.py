import operator

from app.conference_track_management.slot import fill_slot, event
from constants import constants


def process_and_schedule_talks(valid_talks):
    valid_talks = sorted(valid_talks.items(),key=operator.itemgetter(1),reverse=True)
    track_count = 0
    morning_slots = []
    lunch_slots = []
    afternoon_slots = []
    tracks = []
    while(len(valid_talks)!=0):
        morning_slot = fill_slot(constants.TRACK_START_TIME,constants.MORNING_SLOT_DURATION_MINUTES,valid_talks)
        morning_slots.append(morning_slot)
        lunch_slot = event(constants.LUNCH_START_TIME,constants.LUNCH_DURATION_MINUTES,constants.LUNCH_TALK)
        lunch_slots.append(lunch_slot)
        afternoon_slot = fill_slot(constants.POST_LUNCH_SLOT_START_TIME,constants.AFTERNOON_SLOT_DURATION_MINUTES,valid_talks)
        afternoon_slots.append(afternoon_slot)
        track_count += 1
        tracks.append(track_count)
        print(valid_talks)
    print(track_count)
    print(morning_slots)
    print(lunch_slots)
    print(afternoon_slots)
    '''return morning_slots,lunch_slots,afternoon_slot'''
