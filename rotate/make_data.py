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
from submissions.accepted.rotate_dnc import solve

"""
Seed for the random number generator. We need this so randomized tests will
generate the same thing every time. Seeds can be integers or strings.
"""
SEED = 'you can rotate my red black tree ;))'

MAX_T = 100
MAX_N_MAIN = 100
MAX_N_BONUS_1 = 10 ** 6
MAX_N_BONUS_2 = 10 ** 18


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    """
    
    def __init__(self, N, K):
        self.N = N
        self.K = K


def make_sample_tests():
    """
    Make all sample test files.
    
    To create a pair of sample test files, call make_sample_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_sample_test for more info.
    """
    
    main_sample_cases = [
        TestCase(1, 1), # N = 1 edge case
        TestCase(5, 1), # generic, odd N odd K
        TestCase(5, 2), # generic, odd N even K
        TestCase(6, 3), # generic, even N odd K
        TestCase(6, 4), # generic, even N even K
        TestCase(98, 57), # big numbers ft. reva
    ]
    make_sample_test(main_sample_cases, 'main')
    
    bonus_1_sample_cases = [
        TestCase(1337, 420), # haha funny numbers
        TestCase(6666, 999), # haha moar funny numbers
    ]
    make_sample_test(bonus_1_sample_cases, 'bonus_1')

    bonus_2_sample_cases = [
        TestCase(31415926535897932, 3846264338327950), # i liek pi
    ]
    make_sample_test(bonus_2_sample_cases, 'bonus_2')


def make_secret_tests():
    """
    Make all secret test files.
    
    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    """

    def make_random_case(max_N):
        N = random.randint(9 * max_N // 10, max_N)
        K = random.randint(1, N)
        return TestCase(N, K)

    def make_last_card_case(max_N):
        N = random.randint(9 * max_N // 10, max_N)
        return TestCase(N, last_card(N))

    def last_card(N):
        if N == 1:
            return 1
        if N % 2 == 0:
            return last_card(N // 2) * 2 - 1
        else:
            return last_card(N // 2) * 2 + 1

    main_ones = [TestCase(N, 1) for N in range(1, 101)]
    make_secret_test(main_ones, 'main_ones')
    
    main_Ns = [TestCase(N, N) for N in range(1, 101)]
    make_secret_test(main_Ns, 'main_Ns')
    
    main_firsts = [TestCase(1, 1)] + [TestCase(N, 2) for N in range(2, 101)]
    make_secret_test(main_firsts, 'main_firsts')
    
    main_lasts = [TestCase(N, last_card(N)) for N in range(1, 101)]
    make_secret_test(main_lasts, 'main_lasts')
    
    main_rands = [make_random_case(MAX_N_MAIN) for _ in range(MAX_T)]
    make_secret_test(main_rands, 'main_rands')
    
    for i in range(3):
        bonus_1_rands = [make_random_case(MAX_N_BONUS_1)]
        make_secret_test(bonus_1_rands, 'bonus_1_rands')
    
    for i in range(3):
        bonus_1_lasts = [make_last_card_case(MAX_N_BONUS_1)]
        make_secret_test(bonus_1_lasts, 'bonus_1_lasts')
    
    for i in range(3):
        bonus_2_rands = [make_random_case(MAX_N_BONUS_2) for _ in range(MAX_T)]
        make_secret_test(bonus_2_rands, 'bonus_2_rands')
    
    for i in range(3):
        bonus_2_lasts = [make_last_card_case(MAX_N_BONUS_2) for _ in range(MAX_T)]
        make_secret_test(bonus_2_lasts, 'bonus_2_lasts')


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    """
    T = len(cases)
    assert 1 <= T <= 100, f'invalid T: {T}'
    print(T, file=file)
    for case in cases:
        if 'main' in file.name:
            assert 1 <= case.N <= MAX_N_MAIN, f'invalid N for main: {case.N}'
        elif 'bonus_1' in file.name:
            assert 1 <= case.N <= MAX_N_BONUS_1, f'invalid N for bonus 1: {case.N}'
        elif 'bonus_2' in file.name:
            assert 1 <= case.N <= MAX_N_BONUS_2, f'invalid N for bonus 2: {case.N}'
        assert 1 <= case.K <= case.N, f'invalid K: {case.K} (N is {case.N})'
        
        print(f'{case.N} {case.K}', file=file)
    
    sum_N = sum(case.N for case in cases)
    if 'bonus_1' in file.name:
        assert 1 <= sum_N <= MAX_N_BONUS_1, f'invalid total N for bonus 1: {sum_N}'


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    """
    for case in cases:
        print(solve(case.N, case.K), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
