#!/usr/bin/env python
"""
Make zip files for each test set following the DOMjudge zip file format.

To set up this script, do the following:
    - Set PROBLEM_NAME to your problem name.
    - Set TIME_LIMIT for your problem if desired.
    - Set TEST_SET_NAMES to list the names of each test set of your problem.
    - Update is_data_in_test_set
    - Update is_submission_in_test_set
Everything else will be handled by the make_zips function in calico_lib.py.

You can also run this file with the following arguments:
    -v see debug prints
    -d also make data before zipping
    -r create release version without * in DOMjudge name
"""

from calico_lib import make_zips

"""
The short name of the problem.

Names must only use lowercase letters and digits and should be contest-unique.
Names should be short if possible.
"""
PROBLEM_NAME = 'subway'

"""
The time limit in seconds.

Typically this is 1 but feel free to adjust as necessary for your problem.
"""
TIME_LIMIT = 1

"""
A list with strings containing the names of every test set.

The script will generate a zip for each test set. The filter functions below
should only return names from this list.
"""
TEST_SET_NAMES = ['main', 'bonus_1', 'bonus_2']


def is_data_in_test_set(data_file_name, test_set_name):
    """
    Return True if the data (test .in or .ans) file named data_file_name
    should be added to the test set named test_set_name.
    """
    if test_set_name == 'main':
        return 'main' in data_file_name
    elif test_set_name == 'bonus_1':
        return 'main' in data_file_name or 'bonus_1' in data_file_name
    elif test_set_name == 'bonus_2':
        return 'main' in data_file_name or 'bonus' in data_file_name

def is_submission_in_test_set(submission_file_name, test_set_name):
    """
    Return True if the submission file named submission_file_name should be
    added to the test set named test_set_name.
    """
    file_to_sets = {
        # accepted
        'subway_very_slow':     ['main'],
        'subway_naive':         ['main'],
        'subway_ignore':        ['main', 'bonus_1'],
        'subway_dsu_heap':      ['main', 'bonus_1', 'bonus_2'],
        'subway_map_priority':  ['main', 'bonus_1', 'bonus_2'],
        
        # tle
        'subway_very_slow_tle': ['bonus_1', 'bonus_2'],
        'subway_naive_tle':     ['bonus_1', 'bonus_2'],
        'subway_ignore_tle':    ['bonus_2'],
    }
    
    # we only care about actual code files
    if submission_file_name.split('.')[-1] not in ['cpp', 'java', 'py']:
        return False
    
    # trim file extensions
    submission_file_name = submission_file_name.split('.')[0]
    
    return submission_file_name in file_to_sets and test_set_name in file_to_sets[submission_file_name]


def main():
    """
    Let the library do the rest of the work!
    """
    make_zips(PROBLEM_NAME, TIME_LIMIT, TEST_SET_NAMES, \
              is_data_in_test_set, is_submission_in_test_set)


if __name__ == '__main__':
    main()
