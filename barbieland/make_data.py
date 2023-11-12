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
SEED = '†ø∂ø çhåñgé +≠îß †ø ∫0nnë†h1ñg ∂îƒƒé®éñ†, 10¬g, åπ∂ ª®ßi†®a‰¥.'

from graph_randomizer import *

class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    
    TODO Change this to store the relevant information for your problem.
    """


    def __init__(self, N, M, Q, hardcoded_edges= None, hardcoded_queries= None, stability= 10):
        assert stability >= 0
        attractability = [ra.expovariate(1) + stability for _ in range(N)]

        self.N = N
        if hardcoded_edges is not None:
            assert isinstance(hardcoded_edges, list) and len(hardcoded_edges) == M
            assert all([isinstance(edge, tuple) and len(edge) == 2 for edge in hardcoded_edges])
            assert all([0 < edge[0] <= N and 0 < edge[1] <= N for edge in hardcoded_edges])
            self.edges = hardcoded_edges
        else:
            self.graph = GraphRandomizer(range(1, N + 1), M, False, force_edge_lim= False, base_attractibility= attractability)
            self.edges = self.graph.edge_set
            self.M = len(self.edges)

        self.Q = Q
        if hardcoded_queries is not None:
            assert isinstance(hardcoded_queries, list) and len(hardcoded_queries) == Q
            assert all([isinstance(q, tuple) and len(q) == 2 for q in hardcoded_queries])
            assert all([0 < q[0] <= N and 0 < q[1] <= N for q in hardcoded_queries])
            self.queries = hardcoded_queries
        else:
            self.queries = [(ra.randint(1, N), ra.randint(1, N)) for _ in range(Q)]
    
    def assign_edge_weights(self, basis):
        self.edge_weights = {}
        for edge in self.edges:
            w = 0
            basis_bitmask = random.randint(0, 2 ** len(basis) - 1)
            for i in range(len(basis)):
                if basis_bitmask & (1 << i) > 0:
                    w = w ^ basis[i]
            assert 0 <= w <= 10 ** 18
            self.edge_weights[edge] = w
            


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
    # main_sample_cases = [
    #     TestCase(7, 9),
    #     TestCase(420, 69),
    #     TestCase(3, 0),
    # ]
    # make_sample_test(main_sample_cases, 'main')
    pass


def make_secret_tests():
    """
    Make all secret test files.
    
    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    
    TODO Write sample tests. Consider creating edge cases and large randomized
    tests.
    """
    UPPER_LIM = 10 ** 5

    stabilities = [10, 1, 5, 0, 100]
    
    def create_basis(size):
        assert 0 < size <= 59
        return [1 << p for p in random.sample(range(59), size)]
    basis_sizes = [4, 10, 59]

    graph_node_amt_limits = [10 ** 3, 10 ** 4, 10 ** 5]

    graph_edge_amt_funcs = [
        lambda N : min(5 * N // 4, N + 20, UPPER_LIM),
        lambda N : min(3 * N, UPPER_LIM),
        lambda N : min(N * (N - 1) // 2, UPPER_LIM)
    ]

    graph_batches = []
    for basis_size in basis_sizes:
        for node_lim in graph_node_amt_limits:
            for f in graph_edge_amt_funcs:
                batch = []
                N_remain, M_remain = UPPER_LIM, UPPER_LIM
                for stability in stabilities:
                    N = random.randint(9 * node_lim // 10, node_lim)
                    M = f(N)
                    N_remain -= N
                    M_remain -= M
                    if not (N_remain > 0 and M_remain > 0):
                        break
                    batch.append((N, M, basis_size, stability))
                graph_batches.append(batch)
    
    def basis_size_to_name(size):
        return {
            4: 'small_basis',
            10: 'med_basis',
            59: 'max_basis',
        }[size]

    def edge_node_ratio_to_name(N, M):
        if N + 50 > M:
            return 'sparse_graph'
        if M == min(N * (N - 1) // 2, UPPER_LIM):
            return 'max_graph'
        return 'med_graph'

    # FUCK TODO
    # for batch in graph_batches:
    #     avg_Q = UPPER_LIM // len(batch)

    #     test_cases = []
    #     for graph in batch:

    #     make_secret_test('{}_{}'.format(basis_size_to_name()))




def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    
    TODO Implement this for your problem.
    """
    T = len(cases)
    print(T, file=file)
    for case in cases:
        print(f'{case.A} {case.B}', file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    
    TODO Implement this for your problem by changing the import below.
    """
    from submissions.accepted.add_arbitrary import solve
    for case in cases:
        print(solve(case.A, case.B), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
