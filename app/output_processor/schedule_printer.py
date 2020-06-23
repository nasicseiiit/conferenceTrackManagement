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

def print_tracks(track_id):
    print("Track ",track_id,":")

def print_slots(slots):
    if(len(slots)>0):
        for slot in slots:
            print(slot)

def print_events(event):
    if(len(event)>0):
            print(event)