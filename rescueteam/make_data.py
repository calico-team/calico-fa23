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
SEED = 'bespinben i hate you why did you delete your primal dialga piano version pdf now i cant find it im gonna cry'

from graph_randomizer import *

import sys

sys.setrecursionlimit(10 ** 9)


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    
    TODO Change this to store the relevant information for your problem.
    """

    def __init__(self, F, B, N, M, S, E, stability=10, hardcoded_edges=None, hardcoded_treasures=None):
        assert stability >= 0
        attractability = [ra.expovariate(1) + stability for _ in range(N)]
        assert (S != E)
        self.S = S
        self.E = E
        self.N = N
        self.B = B
        if hardcoded_edges is not None:
            assert isinstance(hardcoded_edges, list) and len(hardcoded_edges) == M
            assert all([isinstance(edge, tuple) and len(edge) == 2 for edge in hardcoded_edges])
            assert all([0 < edge[0] <= N and 0 < edge[1] <= N for edge in hardcoded_edges])
            self.edges = hardcoded_edges
            self.M = M
        else:
            self.graph = GraphRandomizer(range(1, N + 1), M, False, force_edge_lim=False,
                                         base_attractibility=attractability)
            self.edges = [(u, v) for u, v in self.graph.edge_set]
            self.M = len(self.edges)

        self.F = F
        if hardcoded_treasures is not None:
            assert isinstance(hardcoded_treasures, list) and len(hardcoded_treasures) == F
            assert all([isinstance(Ri, int) for Ri in hardcoded_treasures])
            assert all([0 < Ri <= N for Ri in hardcoded_treasures])
            assert all([(Ri != S and Ri != E) for Ri in hardcoded_treasures])
            self.treasures = hardcoded_treasures
        else:
            self.treasures = [ra.randint(1, N) for i in range(F)]
            for i in range(F):
                while self.treasures[i] == S or self.treasures[i] == E:
                    self.treasures[i] = ra.randint(1, N)


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
        TestCase(F=3, B=6, N=5, M=5, S=3, E=4,
                 hardcoded_treasures=[1, 2, 5],
                 hardcoded_edges=[(2, 4), (4, 1), (1, 5), (1, 3), (5, 3)]),
        TestCase(F=3, B=12, N=3, M=3, S=3, E=1,
                 hardcoded_treasures=[2, 2, 2],
                 hardcoded_edges=[(3, 2), (3, 1), (2, 1)]),
        TestCase(F=4, B=7, N=6, M=8, S=2, E=6,
                 hardcoded_treasures=[5, 1, 3, 4],
                 hardcoded_edges=[(3, 5), (3, 1), (1, 5), (6, 1), (1, 4), (4, 2), (4, 6), (2, 6)]),
        TestCase(F=4, B=8, N=5, M=6, S=1, E=3,
                 hardcoded_treasures=[4, 2, 2, 5],
                 hardcoded_edges=[(4, 3), (4, 2), (2, 3), (2, 5), (5, 3), (5, 1)]),
        TestCase(F=1, B=3, N=6, M=5, S=2, E=4,
                 hardcoded_treasures=[5],
                 hardcoded_edges=[(1, 6), (5, 1), (1, 4), (3, 5), (2, 3)])
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

    stabilities = [10, 1, 5, 0, 100]
    upper_lim_n = 10 ** 5
    upper_lim_m = 10 ** 5

    graph_node_amt_limits = [10 ** 3, 10 ** 4, 10 ** 5, 10 ** 5, 10 ** 5]

    graph_edge_amt_funcs = [
        lambda N: min(5 * N // 4, N + 20, upper_lim_m),
        lambda N: min(3 * N, upper_lim_m),
        lambda N: min(N * (N - 1) // 2, upper_lim_m)
    ]

    def edge_node_ratio_to_name(N, M):
        if N + 50 > M:
            return 'sparse_graph'
        if M == min(N * (N - 1) // 2, upper_lim_m):
            return 'max_graph'
        return 'med_graph'

    def node_limit_to_name(N):
        if N <= 10 ** 3:
            return 'few_nodes'
        if N <= 10 ** 4:
            return 'medium_nodes'
        return 'many_nodes'

    # Generating cases for main

    upper_lim_f_main = 100
    upper_lim_b_main = 10 ** 3

    for node_lim in graph_node_amt_limits:
        for f in graph_edge_amt_funcs:
            batch = []
            remaining_n = upper_lim_n
            remaining_m = upper_lim_m
            remaining_f = upper_lim_f_main
            remaining_b = upper_lim_b_main
            max_f = upper_lim_f_main * node_lim / upper_lim_n
            max_b = upper_lim_b_main * node_lim / upper_lim_n
            while True:
                stability = random.choice(stabilities)
                N = max(random.randint(9 * node_lim // 10, node_lim), 3)
                M = f(N)
                F = max(random.randint(9 * max_f // 10, max_f), 1)
                B = max(random.randint(9 * max_b // 10, max_b), 1)
                remaining_n -= N
                remaining_m -= M
                remaining_f -= F
                remaining_b -= B
                if not (
                        len(batch) < 100 and remaining_n >= 0 and remaining_m >= 0 and remaining_b >= 0 and remaining_f >= 0):
                    break
                S = random.randint(1, N)
                E = random.randint(1, N)
                while S == E:
                    E = random.randint(1, N)
                batch.append(TestCase(F, B, N, M, S, E, stability=stability))

            make_secret_test(batch, 'main_{}_{}'.format(node_limit_to_name(batch[0].N),
                                                        edge_node_ratio_to_name(batch[0].N, batch[0].M)))

    # TODO EDGE TEST CASES (not edging them just doing them lmao)

    for _ in range(3):
        N = random.randint(9 * upper_lim_n // 10, upper_lim_n)
        F = random.randint(9 * upper_lim_f_main // 10, upper_lim_f_main)
        B = random.randint(9 * upper_lim_b_main // 10, upper_lim_b_main)
        nodes = [i + 1 for i in range(N)]
        random.shuffle(nodes)
        hardcoded_edges = [(nodes[i], nodes[i + 1]) for i in range(N - 1)]
        M = N - 1
        make_secret_test([TestCase(F=F, B=B, N=N, M=M, S=nodes[0], E=nodes[1], hardcoded_edges=hardcoded_edges)],
                         'main_edge')

    for _ in range(3):
        N = 250
        F = random.randint(9 * upper_lim_f_main // 10, upper_lim_f_main)
        B = 125 + _ * N
        nodes = [i + 1 for i in range(N)]
        random.shuffle(nodes)
        hardcoded_edges = [(nodes[i], nodes[i + 1]) for i in range(N - 1)]
        M = N - 1
        make_secret_test([TestCase(F=F, B=B, N=N, M=M, S=nodes[0], E=nodes[-1], hardcoded_edges=hardcoded_edges)],
                         'main_edge_low_b')

    # Generating test cases for bonus

    upper_lim_f_bonus = 10 ** 5
    upper_lim_b_bonus = 10 ** 9

    for node_lim in graph_node_amt_limits:
        for f in graph_edge_amt_funcs:
            batch = []
            remaining_n = upper_lim_n
            remaining_m = upper_lim_m
            remaining_f = upper_lim_f_bonus
            max_f = upper_lim_f_bonus * node_lim / upper_lim_n
            max_b = upper_lim_b_bonus
            while True:
                stability = random.choice(stabilities)
                N = max(random.randint(9 * node_lim // 10, node_lim), 3)
                M = f(N)
                F = max(random.randint(9 * max_f // 10, max_f), 1)
                B = max(random.randint(9 * max_b // 10, max_b), 1)
                remaining_n -= N
                remaining_m -= M
                remaining_f -= F
                if not (len(batch) < 100 and remaining_n >= 0 and remaining_m >= 0 and remaining_f >= 0):
                    break
                S = random.randint(1, N)
                E = random.randint(1, N)
                while S == E:
                    E = random.randint(1, N)
                batch.append(TestCase(F, B, N, M, S, E, stability=stability))

            make_secret_test(batch, 'bonus_{}_{}'.format(node_limit_to_name(batch[0].N),
                                                         edge_node_ratio_to_name(batch[0].N, batch[0].M)))

    # TODO EDGE TEST CASES (not edging them just doing them lmao)

    for _ in range(3):
        N = random.randint(9 * upper_lim_n // 10, upper_lim_n)
        F = random.randint(9 * upper_lim_f_bonus // 10, upper_lim_f_bonus)
        B = random.randint(9 * upper_lim_b_bonus // 1000, upper_lim_b_bonus)
        nodes = [i + 1 for i in range(N)]
        random.shuffle(nodes)
        hardcoded_edges = [(nodes[i], nodes[i + 1]) for i in range(N - 1)]
        M = N - 1
        make_secret_test([TestCase(F=F, B=B, N=N, M=M, S=nodes[0], E=nodes[1], hardcoded_edges=hardcoded_edges)],
                         'bonus_edge')

    for _ in range(5):
        N = random.randint(9 * upper_lim_n // 10, upper_lim_n)
        F = random.randint(9 * upper_lim_f_bonus // 10, upper_lim_f_bonus)
        B = min(N // 2, upper_lim_b_bonus) + _ * (N - 1)
        nodes = [i + 1 for i in range(N)]
        random.shuffle(nodes)
        hardcoded_edges = [(nodes[i], nodes[i + 1]) for i in range(N - 1)]
        M = N - 1
        make_secret_test([TestCase(F=F, B=B, N=N, M=M, S=nodes[0], E=nodes[-1], hardcoded_edges=hardcoded_edges)],
                         'bonus_edge_low_b')


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    
    TODO Implement this for your problem.
    """
    import os
    file_name = os.path.basename(file.name)
    T = len(cases)
    assert T <= 100
    print(T, file=file)
    for case in cases:
        print(f'{case.F} {case.B}', file=file)
        print(f'{case.N} {case.M} {case.S} {case.E}', file=file)
        print(*case.treasures, file=file)
        for u, v in case.edges:
            print(f'{u} {v}', file=file)
        assert case.N <= 10 ** 5 and case.M <= 10 ** 5
        assert case.E != case.S

    if 'main' in file_name:
        assert sum(case.F for case in cases) <= 100
        assert sum(case.B for case in cases) <= 10 ** 3
        assert all([1 <= case.F <= 100 for case in cases])
        assert all([1 <= case.B <= 10 ** 3 for case in cases])
    elif 'bonus' in file_name:
        assert sum(case.F for case in cases) <= 10 ** 5
        assert all([1 <= case.F <= 10 ** 5 for case in cases])
        assert all([1 <= case.B <= 10 ** 9 for case in cases])
        


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    
    TODO Implement this for your problem by changing the import below.
    """
    from submissions.accepted.rescueteam_heap import solve
    for case in cases:
        F = case.F
        B = case.B
        N = case.N
        M = case.M
        S = case.S
        E = case.E
        R = case.treasures
        U = [edge[0] for edge in case.edges]
        V = [edge[1] for edge in case.edges]
        print(solve(F, B, N, M, S, E, R, U, V), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
