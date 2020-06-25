
''' validating the input file
If the line ends with lightning then the duration will be 5 mins to the talk
If the line ends with min then the minimum duration is 1 and the maximum duration is 180
Else the talk will be discarded
'''
from app.constants import constants

def validate_input_data(file_data):
    talks_with_lightning = lines_ending_with(file_data, constants.LIGHTNING)
    talks_with_min = lines_ending_with(file_data, constants.MINUTES)
    map_talk_and_time = {}
    map_talk_and_time = mapping_duration_to_lightning_talk(map_talk_and_time, talks_with_lightning)
    map_talk_and_time = mapping_duration_to_min_talk(map_talk_and_time, talks_with_min)
    return map_talk_and_time
'''
adding the lightning talks 
'''
def mapping_duration_to_lightning_talk(map_talk_and_time, talks_with_lightning):
    for talk in talks_with_lightning:
        map_talk_and_time[talk] = constants.LIGHTNING_DURATION_MINUTES
    return map_talk_and_time
'''
adding the minute talks
'''
def mapping_duration_to_min_talk(map_talk_and_time, talks_with_min):
    SUBTRACT_THREE = 3
    SUBTRACT_ONE = 1
    for line in talks_with_min:
        split_line = line.split()
        minutes_string = split_line[-SUBTRACT_ONE]
        duration = int(minutes_string[:-SUBTRACT_THREE])
        map_talk_and_time[line] = duration
    return map_talk_and_time

def lines_ending_with(file_data, key):
 return (list(filter(lambda line: line.endswith(key), file_data)))