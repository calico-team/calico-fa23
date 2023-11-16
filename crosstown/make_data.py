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

import os
import random
from calico_lib import make_sample_test, make_secret_test, make_data

"""
Seed for the random number generator. We need this so randomized tests will
generate the same thing every time. Seeds can be integers or strings.
"""
SEED = 'big ben sits on a bus for twelve hours'

MAIN_MAX_N = 10
MAIN_MAX_M = 10


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    """

    def __init__(self, N, M, starts, ends):
        self.N = N
        self.M = M
        self.starts = starts
        self.ends = ends


def make_sample_tests():
    """
    Make all sample test files.
    
    To create a pair of sample test files, call make_sample_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_sample_test for more info.
    """
    main_sample_cases = [
        TestCase(
            1, 6,
            [3],
            [5]
        ),
        TestCase(
            2, 6,
            [1, 4],
            [5, 6]
        ),
        TestCase(
            2, 6,
            [1, 4],
            [5, 6]
        ),
        TestCase(
            2, 8,
            [2, 3],
            [6, 5]
        ),
        TestCase(
            4, 5,
            [1, 3, 3, 5],
            [4, 5, 1, 2]
        ),
        TestCase(
            7, 7,
            [1, 1, 1, 1, 1, 1, 1],
            [7, 7, 7, 7, 7, 7, 7]
        ),
    ]
    make_sample_test(main_sample_cases, 'main')


def make_secret_tests():
    """
    Make all secret test files.
    
    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    """

    def get_possible_trip(m):
        return random.sample(range(1, m + 1), k=2)
    

    def random_cases(max_N, max_M, T):
        def case():
            N = random.randint(9 * max_N // 10, max_N)
            M = random.randint(9 * max_M // 10, max_M)
            trips = [get_possible_trip(M) for _ in range(N)]
            starts = [t[0] for t in trips]
            ends = [t[1] for t in trips]
            return TestCase(N, M, starts, ends)
        return [case() for _ in range(T)]
    
    def anti_M(N, M, T):
        def case():
            s, e = get_possible_trip(M)
            starts = [s] * N
            ends = [e] * N
            return TestCase(N, M, starts, ends)
        return [case() for _ in range(T)]

    for i in range(3):
        for _ in range(3):
            make_secret_test(random_cases(MAIN_MAX_N, MAIN_MAX_M, 100), 'main_random')
    
    make_secret_test(anti_M(MAIN_MAX_N, MAIN_MAX_M, 100), f'main_anti_m')

def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    """
    file_name = os.path.basename(file.name)
    
    T = len(cases)
    assert 1 <= T <= 100
    
    print(T, file=file)
    for case in cases:
        print(f'{case.N} {case.M}', file=file)
        
        if 'main' in file_name:
            assert 1 <= case.N <= MAIN_MAX_N
            assert 2 <= case.M <= MAIN_MAX_M
        else:
            # https://cdn.discordapp.com/attachments/1157421192026800179/1174577632671711303/image.png
            raise 'bruh wtf u named ur test file wrong'
        
        print(*case.starts, file=file)
        print(*case.ends, file=file)
        
        assert all(1 <= s <= case.M for s, e in zip(case.starts, case.ends))
        assert all(1 <= e <= case.M for s, e in zip(case.starts, case.ends))
        assert all(s != e for s, e in zip(case.starts, case.ends))


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    """
    from submissions.accepted.crosstown import solve
    for case in cases:
        ans = solve(case.N, case.M, case.starts, case.ends)
        print(ans, file=file)
        
        assert 1 <= ans <= (case.N + 2) * case.M


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()