import unittest

from test.test_cli_arguments import test_for_cli_arguments
from test.test_input_data import test_file_data
from test.test_input_data_validator import test_validate_data
from test.test_slot import test_slot

''' test suite to run the all test cases'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_for_cli_arguments('test_get_file_name'))
    suite.addTest(test_file_data('test_check_file_existance'))
    suite.addTest(test_file_data('test_check_file_existance_error'))
    suite.addTest(test_file_data('test_get_file_data'))
    suite.addTest(test_file_data('test_get_file_data_empty_list'))
    suite.addTest(test_validate_data('test_mapping_duration_to_lightning_talk'))
    suite.addTest(test_validate_data('test_mapping_duration_to_min_talk'))
    suite.addTest(test_validate_data('test_validate_input_data'))
    suite.addTest(test_slot('test_fill_slot'))
    suite.addTest(test_slot('test_event'))
    suite.addTest(test_slot('test_has_room'))
    suite.addTest(test_slot('test_has_room_returns_false'))


    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())