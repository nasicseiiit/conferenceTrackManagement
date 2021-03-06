from app.conference_track_management.conference_manager import process_and_schedule_talks
from app.reader.cli_rguments import get_cli_arguments
from app.reader.input_data import get_file_data
from app.validator.input_data_validator import validate_input_data
from app.writer.schedule_printer import print_schedule

#main method
def main():
    file_name = get_cli_arguments()
    file_data = get_file_data(file_name)
    valid_talks = validate_input_data(file_data)
    [tracks, morning_sessions, lunch_sessions, afternoon_sessions, network_events] = process_and_schedule_talks(valid_talks)
    print_schedule(tracks, morning_sessions, lunch_sessions, afternoon_sessions, network_events)

if __name__ == "__main__":
    main()