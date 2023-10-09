
"""
Make test data for the problem.

To set up this script, do the following:
    - Set the seed to be something different, long, and arbitrary.
    - Set up the TestCase class to hold relevant information for your problem.
    - Write sample and secret tests in their respective functions.
    - Write input and output code in their respective functions.
Everything else will be handled by the make_data function in calico_lib.py.

You can also run this file with the -v argument to see debug prints.
"""

import random

import numpy as np

from calico_lib import make_sample_test, make_secret_test, make_data
from submissions.accepted.benga_numpy import solve

"""
Seed for the random number generator. We need this so randomized tests will
generate the same thing every time. Seeds can be integers or strings.
"""
SEED = 'TODO Change this to something different, long, and arbitrary.'

MAX_T = 100
MAX_N_MAIN = 10 ** 18
MAX_N_BONUS = 10 ** (10 ** 6)
MOD = 2 ** (3 ** 2) * 3 ** (2 ** 3)


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    """
    
    def __init__(self, N):
        self.N = N


def make_sample_tests():
    """
    Make all sample test files.
    
    To create a pair of sample test files, call make_sample_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_sample_test for more info.
    """
    
    main_sample = [
        TestCase(2),
        TestCase(3),
        TestCase(6),
        TestCase(11),
        TestCase(16),
        TestCase(369),
        TestCase(333333333333333333),
    ]
    make_sample_test(main_sample, 'main_sample')
    
    bonus_sample = [
        TestCase(314159265358979323846264338327950288419716939937510582),
    ]
    make_sample_test(bonus_sample, 'bonus_sample')


def make_secret_tests():
    """
    Make all secret test files.
    
    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    """


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    """
    
    T = len(cases)
    assert 1 <= T <= MAX_T
    print(T, file=file)
    for case in cases:
        if 'main' in file.name:
            assert 1 <= case.N <= MAX_N_MAIN
        elif 'bonus' in file.name:
            assert 1 <= case.N <= MAX_N_BONUS
        print(f'{case.N}', file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    """
    
    for case in cases:
        ans = solve(case.N)
        assert 0 <= ans <= MOD
        print(ans, file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
