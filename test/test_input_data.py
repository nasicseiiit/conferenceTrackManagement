import os
import unittest

from app.reader.input_data import get_file_data, check_file_existance


class test_file_data(unittest.TestCase):
    current_directory = os.getcwd()
    file_name = (os.path.abspath(os.path.join(current_directory, os.pardir)))
    '''
    test case with a valid file name
    '''
    def test_check_file_existance(self):
        file_name = self.file_name + "/app/input_data/input_file"
        pointer_to_file = check_file_existance(file_name)
        self.assertNotEqual(pointer_to_file, False)
        pointer_to_file.close()

    '''
        test case with a invalid file
    '''

    def test_check_file_existance_error(self):
        file_name = self.file_name + "/app/input_data/ramdom_file"
        pointer_to_file = check_file_existance(file_name)
        self.assertEqual(pointer_to_file, False)

    '''
    test case to read the input_data from the input file
    '''
    def test_get_file_data(self):
        file_name = self.file_name + "/app/input_data/test_input_file"
        expected_file_data = ["Writing Fast Tests Against Enterprise Rails 60min","Overdoing it in Python lightningjfjdk","Rails for Python Developers lightning"]
        actual_file_data = get_file_data(file_name)
        self.assertEqual(expected_file_data, actual_file_data)

    '''
        test case to read the input_data from the input file if the file does not exist
    '''
    def test_get_file_data_empty_list(self):
        file_name = self.file_name + "/app/input_data/random_file"
        expected_file_data = []
        actual_file_data = get_file_data(file_name)
        self.assertEqual(expected_file_data, actual_file_data)

if __name__ == '__main__':
    unittest.main()
