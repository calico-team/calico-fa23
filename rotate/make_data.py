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

import random as ra
from calico_lib import make_sample_test, make_secret_test, make_data

"""
Seed for the random number generator. We need this so randomized tests will
generate the same thing every time. Seeds can be integers or strings.
"""
SEED = 'you can rotate my red black tree ;))'


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    
    TODO Change this to store the relevant information for your problem.
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
        TestCase(10, 2),
        TestCase(7, 5),
        TestCase(6, 3),
    ]
    make_sample_test(main_sample_cases, 'main')
    
    bonus_sample_cases = [
        TestCase(66666, 9999),
        TestCase(42069, 11569),
    ]
    make_sample_test(bonus_sample_cases, 'bonus_1')

    bonus_sample_cases = [
        TestCase(31415926535897932, 3846264338327950),
    ]
    make_sample_test(bonus_sample_cases, 'bonus_2')


def make_secret_tests():
    """
    Make all secret test files.
    
    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    """

    def make_random_case(max_digits):
        def random_n_digit_number(n):
            return ra.randint(10 ** (n - 1), (10 ** n) - 1) if n != 0 else 0
        A_digits = ra.randint(1, max_digits)
        B_digits = ra.randint(1, max_digits)
        A, B = random_n_digit_number(A_digits), random_n_digit_number(B_digits)
        return TestCase(max(A, B), min(A, B))
    
    def e():
        return ra.random()
    
    def o(x):
        return ra.randint(1, x)

    T = 100

    test_cases = []
    for _ in range(T):
        test_cases.append(make_random_case(2))
    
    make_secret_test(test_cases, 'main_fuzz')

    test_cases = []
    for N in range(1, 101):
        test_cases.append(TestCase(N, o(N)))
    
    make_secret_test(test_cases, 'main_ascending')

    test_cases = []
    for _ in range(T):
        test_cases.append(make_random_case(4))
    
    make_secret_test(test_cases, 'bonus_1_fuzz')

    test_cases = []
    for _ in range(T):
        test_cases.append(make_random_case(17))
    
    make_secret_test(test_cases, 'bonus_2_fuzz')

    """
    main_edge_cases = [
        TestCase(0, 0),
        TestCase(1, 0),
        TestCase(0, 1),
        TestCase(10 ** 9, 0),
        TestCase(0, 10 ** 9),
        TestCase(10 ** 9, 10 ** 9),
    ]
    make_secret_test(main_edge_cases, 'main_edge')
    
    for i in range(5):
        main_random_cases = [make_random_case(9) for _ in range(100)]
        make_secret_test(main_random_cases, 'main_random')
    
    bonus_edge_cases = [
        TestCase(10 ** 100, 0),
        TestCase(0, 10 ** 100),
        TestCase(10 ** 100, 10 ** 100),
    ]
    make_secret_test(bonus_edge_cases, 'bonus_edge')
    
    for i in range(5):
        bonus_random_cases = [make_random_case(100) for _ in range(100)]
        make_secret_test(bonus_random_cases, 'bonus_random')
    """


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    """
    T = len(cases)
    print(T, file=file)
    for case in cases:
        assert case.N <= 10 ** 18, "N too high"
        assert case.K <= case.N, f"K greater than N: {case.K} > {case.N}"
        print(f'{case.N} {case.K}', file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    """
    from submissions.accepted.rotate_dnc import solve
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
