
import unittest

from app.input_processor.input_data import get_file_data, check_file_existance
from app.input_processor.input_data_validator import mapping_duration_to_lightning_talk, mapping_duration_to_min_talk, \
    is_valid_duration, validate_input_data


class test_file_data(unittest.TestCase):
    '''
    test case to map duration time to lightning talk
    '''
    def test_mapping_duration_to_lightning_talk(self):
        map_talk_and_time = {}
        talks_with_lightning = ["Rails for Python Developers lightning"]
        expected_answer = {'Rails for Python Developers lightning': 5}
        actual_answer = mapping_duration_to_lightning_talk(map_talk_and_time, talks_with_lightning)
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)

    '''
        test case to map duration time to min talk
        '''
    def test_mapping_duration_to_min_talk(self):
        map_talk_and_time = {'Rails for Python Developers lightning': 5}
        talks_with_min = ["Writing Fast Tests Against Enterprise Rails 60min"]
        expected_answer = {'Rails for Python Developers lightning': 5, 'Writing Fast Tests Against Enterprise Rails 60min': 60}
        actual_answer = mapping_duration_to_min_talk(map_talk_and_time, talks_with_min)
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)

    '''
            test case to check is the duration is valid with valid duration time
            '''
    def test_is_valid_duration(self):
        duration = 23
        expected_answer = True
        actual_answer = is_valid_duration(duration)
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)

    '''
                test case to check is the duration is valid with invalid duration time
                '''

    def test_is_valid_duration(self):
        duration = 1123
        expected_answer = False
        actual_answer = is_valid_duration(duration)
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)

    def test_validate_input_data(self):
        file_data = ["Writing Fast Tests Against Enterprise Rails 60min","Overdoing it in Python lightningjfjdk","Rails for Python Developers lightning"]
        expected_answer = {'Rails for Python Developers lightning': 5,
                           'Writing Fast Tests Against Enterprise Rails 60min': 60}
        actual_answer = validate_input_data(file_data)
        print(actual_answer)
        self.assertEqual(expected_answer, actual_answer)

if __name__ == '__main__':
    unittest.main()
