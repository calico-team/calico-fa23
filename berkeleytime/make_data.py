#!/usr/bin/env python
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
from calico_lib import make_sample_test, make_secret_test, make_data

"""
Seed for the random number generator. We need this so randomized tests will
generate the same thing every time. Seeds can be integers or strings.
"""
SEED = 'out of respect for our founder, we will be starting berkeleyberkeleyberkeley...time'


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
    main_sample_cases = [
        TestCase(20),
        TestCase(500),
        TestCase(180),
        TestCase(80),
        TestCase(30),
        TestCase(0)
    ]
    make_sample_test(main_sample_cases, 'main')
    

def make_secret_tests():
    """
    Make all secret test files.
    
    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    tests.
    """   
    def make_random_case(max_num):
        multiples_10 = []
        for i in range(0, max_num + 1, 10):
            multiples_10.append(i)
        random.shuffle(multiples_10)
        return [TestCase(x) for x in multiples_10]
    
    main_edge_cases = [
        TestCase(0),
        TestCase(500),
        TestCase(170),
    ]
    make_secret_test(main_edge_cases, 'main_edge')
    
    make_secret_test(make_random_case(500), 'main_random')


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    """
    T = len(cases)
    print(T, file=file)
    assert T == len(cases), 'Invalid value of T = {} when there are/were {} test case(s)'.format(T, len(cases))
    for case in cases:
        assert 0 <= case.N <= 500, 'N = {} out of range'.format(case.N)
        assert case.N % 10 == 0, 'N = {} not a multiple of 10'.format(case.N)
        print(f'{case.N}', file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    """
    from submissions.accepted.berkeley_time_solution import solve
    for case in cases:
        print(solve(case.N), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
