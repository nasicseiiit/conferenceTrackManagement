
''' validating the input file
If the line ends with lightning then the duration will be 5 mins to the talk
If the line ends with min then the minimum duration is 1 and the maximum duration is 180
Else the talk will be discarded
'''
from constants import constants


def validate_input_data(file_data):
    talks_with_lightning = (list(filter(lambda line: line.endswith("lightning"), file_data)))
    talks_with_min = (list(filter(lambda line: line.endswith("min"), file_data)))
    map_talk_and_time = {}
    map_talk_and_time = mapping_duration_to_lightning_talk(map_talk_and_time,talks_with_lightning)
    map_talk_and_time = mapping_duration_to_min_talk(map_talk_and_time, talks_with_min)
    return map_talk_and_time

def mapping_duration_to_lightning_talk(map_talk_and_time, talks_with_lightning):
    for talk in talks_with_lightning:
        map_talk_and_time[talk] = constants.LIGHTNING_DURATION
    return map_talk_and_time

def mapping_duration_to_min_talk(map_talk_and_time, talks_with_min):
    SUBTRACT_THREE = 3
    SUBTRACT_ONE = 1
    for line in talks_with_min:
        split_line = line.split()
        minutes_string = split_line[-SUBTRACT_ONE]
        duration = int(minutes_string[:-SUBTRACT_THREE])
        if(is_valid_duration(duration)):
            map_talk_and_time[line] = duration
    return map_talk_and_time

def is_valid_duration(duration):
    return (duration>=constants.MIN_DURATION and duration<=constants.MAX_DURATION)