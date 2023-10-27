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
SEED = 'rohan i miss you so much please unblock me and let me see my children please please please pweeeaseee :3'


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    
    TODO Change this to store the relevant information for your problem.
    """


    def __init__(self, N):
        self.N = N


def make_sample_tests():
    """
    Make all sample test files.
    
    To create a pair of sample test files, call make_sample_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_sample_test for more info.
    
    TODO Write sample tests. Consider creating cases that help build
    understanding of the problem, help with debugging, or possibly help
    identify edge cases.
    """
    main_sample_cases = [
        TestCase(2),
        TestCase(3),
        TestCase(6),
        TestCase(11),
        TestCase(16),
        TestCase(369),
    ]
    make_sample_test(main_sample_cases, 'main')
    
    bonus_sample_cases = [
        TestCase(3359232),
        TestCase(333333333333333333),
    ]
    make_sample_test(bonus_sample_cases, 'bonus')


def make_secret_tests():
    """
    Make all secret test files.
    
    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    
    TODO Write sample tests. Consider creating edge cases and large randomized
    tests.
    """
    def make_random_case(digits):
        def random_n_digit_number(n):
            return random.randint(10 ** (n - 1), (10 ** n) - 1) if n != 0 else 0
        N = random_n_digit_number(digits)
        return TestCase(N)
    
    for i in range(5):
        main_random_multiple_small_cases = [make_random_case(2) for _ in range(10)]
        make_secret_test(main_random_multiple_small_cases, 'main_random_multiple_small')
        main_random_one_big_case = [make_random_case(3)]
        make_secret_test(main_random_one_big_case, 'main_random_one_big')
    
    for i in range(10):
        bonus_random_cases = [make_random_case(18) for _ in range(10)]
        make_secret_test(bonus_random_cases, 'bonus_random')


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    
    TODO Implement this for your problem.
    """
    T = len(cases)
    print(T, file=file)
    for case in cases:
        print(f'{case.N}', file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    
    TODO Implement this for your problem by changing the import below.
    """
    from submissions.accepted.jenga_binpow import solve
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
