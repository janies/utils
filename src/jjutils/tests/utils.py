import logging
import os
import unittest

from jjutils.utils import *


VALID_CSV_FILE_NAME = "testData/csv/valid.csv"
INVALID_CSV_FILE_NAME = "testData/csv/not_a_file.csv"

BAD_CSV_FILE_NAME = "testData/csv/invalid.csv"

VALID_CSV_LINES = [
 {' SecondColumn': ' row1Column2', 'FirstColumn': 'row1Column1'},
 {' SecondColumn': ' row2Column2', 'FirstColumn': 'row2Column1'},
 {' SecondColumn': ' row3Column2', 'FirstColumn': 'row3Column1'},
 {' SecondColumn': ' row4Column2', 'FirstColumn': 'row4Column1'}
]

class test_utils(unittest.TestCase):

    def test_csv_file_to_list_valid(self):
        a = csv_file_to_list(VALID_CSV_FILE_NAME)
        for count, line in enumerate(a):
            assert(line == VALID_CSV_LINES[count])

    def test_csv_file_not_found(self):
        self.assertRaises(IOError, csv_file_to_list, (INVALID_CSV_FILE_NAME))

    def test_csv_invalid_file(self):
        a = csv_file_to_list(BAD_CSV_FILE_NAME)
        for count, line in enumerate(a):
            assert(line == VALID_CSV_LINES[count])
