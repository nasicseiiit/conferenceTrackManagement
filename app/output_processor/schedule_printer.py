'''
printing the conference schedule
'''

def print_schedule(tracks, morning_slots, lunch_slots, afternoon_slots, network_events):
    for i in range(len(tracks)):
        print_tracks(tracks[i])
        print_slots(morning_slots[i])
        print_events(lunch_slots[i])
        print_slots(afternoon_slots[i])
        print_events(network_events[i])
        print()

'''
printing the tracks 
'''
def print_tracks(track_id):
    track = "Track "+str(track_id)+":"
    print(track)

'''
printing the sessions
'''
def print_slots(sessions):
    if(len(sessions)>0):
        for session in sessions:
            print(session)
'''
printing the events
'''
def print_events(event):
    if(len(event)>0):
            print(event)