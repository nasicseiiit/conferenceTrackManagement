from app.utility.clendar_utils import get_calendar_time, get_start_time


def fill_slot(start_time,duration,talks):
    slot_talks = []
    i=0
    while(i<len(talks)):
        minutes = talks[i][1]
        talk = talks[i][0]
        if(has_room(minutes,duration)):
            slot_talk = event(start_time,duration,talk)
            start_time = get_start_time(start_time, minutes)
            slot_talks.append(slot_talk)
            duration -= talks[i][1]
            del talks[i]
        i+=1
    return slot_talks
def event(start_time,duration,talk):
    return str(start_time.time())[0:-3]+" "+str(talk)

def has_room(talk_duration,duration):
    return (talk_duration<=duration)


