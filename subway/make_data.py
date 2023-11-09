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
SEED = 'fund bay area transit'


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    
    TODO Change this to store the relevant information for your problem.
    """


    def __init__(self, N, M, K, starts, ends, pos):
        self.N = N
        self.M = M
        self.K = K
        self.starts = starts
        self.ends = ends
        self.pos = pos


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
        TestCase(5, 5, 1, [3, 3, 3, 3, 3], [2, 2, 2, 2, 2], [4, 3, 1, 5, 2]),
    ]
    make_sample_test(main_sample_cases, 'main')
    
def make_secret_tests():
    """
    Make all secret test files.
    
    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    
    TODO Write sample tests. Consider creating edge cases and large randomized
    tests.
    """

    def get_possible_trip(m):
        return random.randint(1, m), random.randint(1, m)
    
    def choose_k(i, n):
        if i % 3 == 0:
            return 1
        elif i % 3 == 1:
            return int(pow(n, 0.5))
        return n

    def case_generator(max_n, max_m, T, file_num):

        cases = []
        for j in range(T):
            starts = []
            ends = []
            passengers = random.randint(1, max_n) # N
            stations = random.randint(2, max_m) # M
            capacity = choose_k(file_num, passengers)
            starts_by_station = {m: [] for m in range(1, stations + 1)}

            pos = [0] * passengers
            station_counts = [0] * stations

            for p in range(passengers):
                start, end = get_possible_trip(stations)
                starts.append(start)
                ends.append(end)
                station_counts[start - 1] += 1
                starts_by_station[start].append(p)

            for m in range(stations):
                if station_counts[m] > 1:
                    positions = list(range(1, station_counts[m] + 1))
                    random.shuffle(positions)

                    for n in starts_by_station[m + 1]:
                        pos[n] = positions.pop(0)

                elif station_counts[m] == 1:
                    for n in starts_by_station[m + 1]:
                        pos[n] = 1

            cases.append(TestCase(passengers, stations, capacity, starts, ends, pos))
            return cases





    for i in range(10):
        main_random_cases = case_generator(10, 10, 100, i)
        make_secret_test(main_random_cases, 'main_random')
    

    for i in range(10):
        bonus1_random_cases = case_generator(100, 1000, 100, i)
        make_secret_test(bonus1_random_cases, 'bonus1_random')
    

    for i in range(20):
        print(i)
        bonus2_random_cases = case_generator(100000, 100000, 1, i)
        make_secret_test(bonus2_random_cases, 'bonus2_random')
    
    
    
    
    
    


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    
    TODO Implement this for your problem.
    """
    T = len(cases)
    print(T, file=file)
    for case in cases:
        print(f'{case.N} {case.M} {case.K}', file=file)
        print(*case.starts, file=file)
        print(*case.ends, file=file)
        print(*case.pos, file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    
    TODO Implement this for your problem by changing the import below.
    """
    from submissions.accepted.subway_dictionary import solve
    for case in cases:
        print(solve(case.N, case.M, case.K, case.starts, case.ends, case.pos), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
