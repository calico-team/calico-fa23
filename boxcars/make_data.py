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
        self.distribution = sorted(distribution)


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
    impossible_case = pair_sums([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6])
    impossible_case[-1] -= 1
    main_sample_cases = [
        TestCase(pair_sums([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6])),
        TestCase(pair_sums([1, 1, 3, 3, 3, 6], [1, 3, 4, 4, 6, 11])),
        TestCase(pair_sums([21, 38, 27, 25, 8, 7], [15, 12, 5, 35, 12, 14])),
        TestCase(pair_sums([270, 4, 530, 132, 255, 454], [279, 404, 82, 138, 358, 90])),
        TestCase(impossible_case)
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

    main_T = 5
    bonus_T = 100

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
        possible = random.randint(0, 3)
        return random_possible_case() if possible > 0 else random_impossible_case()

    for i in range(10):
        main_random_cases = [random_test_case() for _ in range(main_T)]
        make_secret_test(main_random_cases, 'main_random')

    for i in range(10):
        main_random_cases = [random_impossible_case() for _ in range(main_T)]
        make_secret_test(main_random_cases, 'main_edge')

    for i in range(10):
        main_random_cases = [random_test_case() for _ in range(bonus_T)]
        make_secret_test(main_random_cases, 'bonus_random')

    for i in range(10):
        main_random_cases = [random_impossible_case() for _ in range(bonus_T)]
        make_secret_test(main_random_cases, 'bonus_edge')


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    
    TODO Implement this for your problem.
    """
    T = len(cases)
    print(T, file=file)
    for case in cases:
        assert len(case.distribution) == 36
        assert all([2 <= Si <= 10 ** 9 for Si in case.distribution])
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
        import collections

        def dfs(S, index, A, B):
            counter = collections.Counter(S)
            for a in A:
                for b in B:
                    counter[a + b] -= 1
                    if counter[a + b] < 0:
                        return False

            if len(A) == 6 and len(B) == 6:
                return A, B

            for c in counter:
                if counter[c] != 0:
                    break

            if len(A) < 6:
                result = dfs(S, index + 1, [*A, c], B)
                if result:
                    return result

            if len(B) < 6:
                result = dfs(S, index + 1, A, [*B, c])
                if result:
                    return result

            return False

        def solve(S: list[int]):
            S = [i - 2 for i in S]
            S0 = S[0]
            S = [i - S0 for i in S]

            result = dfs(S, 2, [0, S[1]], [0])
            if not result:
                print("IMPOSSIBLE", file=file)
                return

            A, B = result
            print(' '.join(map(str, [a + 1 + S0 for a in A])), file=file)
            print(' '.join(map(str, [b + 1 for b in B])), file=file)

        solve(case.distribution)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
