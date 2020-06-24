from app.utility.calendar_utils import get_start_time

'''
filling the sessions with the talks
'''
def fill_slot(start_time, session_duration, talks):
    slot_talks = []
    index = 0
    while(index < len(talks) and session_duration>0):
        talk_duration = talks[index][1]
        talk = talks[index][0]
        [index, start_time, session_duration, slot_talks, talks] = adding_talk_to_session(slot_talks, index, talk_duration, session_duration, start_time, talk, talks)
        index += 1
    return slot_talks

'''
adding the event to the session with the time and talk
'''
def event(start_time,talk):
    upto_last_third_char = -3
    time_and_talk = str(start_time.time())[0:upto_last_third_char]+" "+str(talk)
    return time_and_talk

'''
checking whether the talk have the room or not
'''
def has_room(talk_duration,session_duration):
    return (talk_duration <= session_duration)

def adding_talk_to_session(slot_talks, index, talk_duration, session_duration, start_time, talk, talks):
    if (has_room(talk_duration, session_duration)):
        slot_talk = event(start_time, talk)
        start_time = get_start_time(start_time, talk_duration)
        slot_talks.append(slot_talk)
        session_duration -= talk_duration
        del talks[index]
        index -= 1
    return index, start_time, session_duration, slot_talks, talks