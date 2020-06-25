import operator

from app.conference_track_management.session import fill_session, event
from app.constants import constants

'''
scheduling the conference with the talks
'''
def process_and_schedule_talks(valid_talks):
    valid_talks = sorted(valid_talks.items(), key=operator.itemgetter(1), reverse=True)
    track_count = 0
    morning_sessions = []
    lunch_sessions = []
    afternoon_sessions = []
    network_events = []
    tracks = []
    while(len(valid_talks)!=0):
        morning_session = fill_session(constants.TRACK_START_TIME, constants.MORNING_SLOT_DURATION_MINUTES, valid_talks)
        morning_sessions.append(morning_session)
        lunch_session = event(constants.LUNCH_START_TIME, constants.LUNCH_TALK)
        lunch_sessions.append(lunch_session)
        afternoon_session = fill_session(constants.POST_LUNCH_SLOT_START_TIME, constants.AFTERNOON_SLOT_DURATION_MINUTES, valid_talks)
        afternoon_sessions.append(afternoon_session)
        network_events.append(event(constants.NETWORKING_START_TIME, constants.NWTWORKING_EVENT))
        track_count += 1
        tracks.append(track_count)
    return tracks, morning_sessions, lunch_sessions, afternoon_sessions, network_events