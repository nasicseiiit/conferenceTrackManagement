
import unittest

from app.reader.input_data_validator import mapping_duration_to_lightning_talk, mapping_duration_to_min_talk, \
     validate_input_data


class test_validate_data(unittest.TestCase):
    '''
    test case to map duration time to lightning talk
    '''
    def test_mapping_duration_to_lightning_talk(self):
        map_talk_and_time = {}
        talks_with_lightning = ["Rails for Python Developers lightning"]
        expected_answer = {'Rails for Python Developers lightning': 5}
        actual_answer = mapping_duration_to_lightning_talk(map_talk_and_time, talks_with_lightning)
        self.assertEqual(expected_answer, actual_answer)

    '''
        test case to map duration time to min talk
        '''
    def test_mapping_duration_to_min_talk(self):
        map_talk_and_time = {'Rails for Python Developers lightning': 5}
        talks_with_min = ["Writing Fast Tests Against Enterprise Rails 60min"]
        expected_answer = {'Rails for Python Developers lightning': 5, 'Writing Fast Tests Against Enterprise Rails 60min': 60}
        actual_answer = mapping_duration_to_min_talk(map_talk_and_time, talks_with_min)
        self.assertEqual(expected_answer, actual_answer)

    def test_validate_input_data(self):
        file_data = ["Writing Fast Tests Against Enterprise Rails 60min","Overdoing it in Python lightningjfjdk","Rails for Python Developers lightning"]
        expected_answer = {'Rails for Python Developers lightning': 5,
                           'Writing Fast Tests Against Enterprise Rails 60min': 60}
        actual_answer = validate_input_data(file_data)
        self.assertEqual(expected_answer, actual_answer)

if __name__ == '__main__':
    unittest.main()
