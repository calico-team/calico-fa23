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
import itertools
import numpy as np

"""
Seed for the random number generator. We need this so randomized tests will
generate the same thing every time. Seeds can be integers or strings.
"""
SEED = 'two dice, thirty-six numbers; the rule is what is thirty-six minus two?'


def pair_sums(d1, d2):
    return sorted(a + b for a in d1 for b in d2)


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    
    TODO Change this to store the relevant information for your problem.
    """

    def __init__(self, distribution):
        self.distribution = distribution


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
        TestCase(pair_sums([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6])),
        TestCase(pair_sums([1, 1, 3, 3, 3, 6], [1, 3, 4, 4, 6, 11])),
        TestCase(pair_sums([21, 38, 27, 25, 8, 7], [15, 12, 5, 35, 12, 14])),
        TestCase(pair_sums([270, 4, 530, 132, 255, 454], [279, 404, 82, 138, 358, 90]))
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

    def random_dice():
        a = [random.randint(1, 5 * 10 ** 8) for _ in range(6)]
        b = [random.randint(1, 5 * 10 ** 8) for _ in range(6)]
        return a, b

    def random_dice_repetitions():
        a = [random.randint(1, 6) for _ in range(4)] + [random.randint(1, 5 * 10 ** 8)] * 2
        b = [random.randint(1, 6) for _ in range(5)] + [random.randint(1, 5 * 10 ** 8)]
        return a, b

    def random_possible_case():
        rng = random.randint(1, 5)
        d1, d2 = random_dice() if rng < 5 else random_dice_repetitions()
        distribution = pair_sums(d1, d2)
        return TestCase(distribution)

    def random_impossible_case():
        rng = random.randint(1, 5)
        d1, d2 = random_dice() if rng < 5 else random_dice_repetitions()
        distribution = pair_sums(d1, d2)
        if distribution[35] != 2:
            distribution[35] -= 1  # Maybe this makes some solutions impossible??
            distribution.sort()
        return TestCase(distribution)

    def random_test_case():
        rng = random.randint(1, 5)
        d1, d2 = random_dice() if rng < 5 else random_dice_repetitions()
        distribution = pair_sums(d1, d2)
        possible = random.randint(0, 3)
        if possible == 0 and distribution[35] != 2:
            distribution[35] -= 1  # Maybe this makes some solutions impossible??
            distribution.sort()
        return TestCase(distribution)

    for i in range(10):
        main_random_cases = [random_test_case() for _ in range(10)]
        make_secret_test(main_random_cases, 'main_random')

    for i in range(10):
        main_random_cases = [random_impossible_case() for _ in range(10)]
        make_secret_test(main_random_cases, 'main_edge')



def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    
    TODO Implement this for your problem.
    """
    T = len(cases)
    print(T, file=file)
    for case in cases:
        print(*case.distribution, file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    
    TODO Implement this for your problem by changing the import below.
    """
    for case in cases:
        def solve(S: list[int]):
            # suppose we assign S[1] to s12
            a, b = [1, S[1] - S[0] + 1, 0, 0, 0, 0], [S[0] - 1, 0, 0, 0, 0, 0]
            if check(S, a, b):
                print(*a, file=file)
                print(*b, file=file)
                return

            # suppose we assign S[1] to s21
            a, b = [1, 0, 0, 0, 0, 0], [S[0] - 1, S[1] - 1, 0, 0, 0, 0]
            a, b = b, a  # transpose so that s12 is assigned
            if check(S, a, b):
                print(*a, file=file)
                print(*b, file=file)
                return

            print('IMPOSSIBLE', file=file)

        def check(S, a, b):
            """
            Assuming that s11 and s12 have been assigned, and thus a1, a2, and b1 have
            also been assigned, try every possible s13..s16 to check if an assignment of
            S to the rest of the table exists.

            Returns True with the assignment stored in a and b if found.
            """
            for i13_i14_i15_i16 in itertools.combinations(range(2, 31), 4):
                remaining = [S[i] for i in range(2, 36) if i not in i13_i14_i15_i16]
                a[2:] = [S[i] - b[0] for i in i13_i14_i15_i16]
                try:
                    for i in range(1, 6):
                        b[i] = remaining.pop(0) - a[0]
                        for j in range(1, 6):
                            remaining.remove(b[i] + a[j])
                    return True
                except ValueError:
                    pass
            return False

        solve(case.distribution)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
