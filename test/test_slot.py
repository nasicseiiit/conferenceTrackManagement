
import unittest

from app.conference_track_management.slot import fill_slot, event, has_room
from app.constants import constants

class test_slot(unittest.TestCase):
    '''
    test case to fill the slot with the talk
    '''
    def test_fill_slot(self):
        start_time = constants.TRACK_START_TIME
        session_duration = constants.MORNING_SLOT_DURATION_MINUTES
        talks = [('Writing Fast Tests Against Enterprise Rails 60min', 60), ('Rails for Python Developers lightning', 5)]
        expected_answer = ['09:00 Writing Fast Tests Against Enterprise Rails 60min', '10:00 Rails for Python Developers lightning']
        actual_answer = fill_slot(start_time, session_duration, talks)
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)

    '''
        test case to create the event 
        '''
    def test_event(self):
        start_time = constants.TRACK_START_TIME
        talk = "Writing Fast Tests Against Enterprise Rails 60min"
        expected_answer = "09:00 Writing Fast Tests Against Enterprise Rails 60min"
        actual_answer = event(start_time, talk)
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)


    def test_has_room(self):
        talk_duration = 60
        session_duration = 180
        self.assertTrue(has_room(talk_duration,session_duration))

    '''
            test case to check has room or not "by returning false"
            '''
    def test_has_room_returns_false(self):
        talk_duration = 180
        session_duration = 60
        self.assertFalse(has_room(talk_duration,session_duration))

if __name__ == '__main__':
    unittest.main()
