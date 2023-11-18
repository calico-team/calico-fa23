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

import sys

sys.setrecursionlimit(10 ** 9)


def random_weight(basis):
    w = 0
    basis_bitmask = random.randint(0, 2 ** len(basis) - 1)
    for i in range(len(basis)):
        if basis_bitmask & (1 << i) > 0:
            w = w ^ basis[i]
    assert 0 <= w <= 10 ** 18
    return w


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    
    TODO Change this to store the relevant information for your problem.
    """

    def __init__(self, N, M, Q, basis, stability=10, hardcoded_edges=None, hardcoded_queries=None):
        assert stability >= 0
        attractability = [ra.expovariate(1) + stability for _ in range(N)]

        self.N = N
        if hardcoded_edges is not None:
            assert isinstance(hardcoded_edges, list) and len(hardcoded_edges) == M
            assert all([isinstance(edge, tuple) and len(edge) == 3 for edge in hardcoded_edges])
            assert all([0 < edge[0] <= N and 0 < edge[1] <= N and 0 <= edge[2] <= 10 ** 18 for edge in hardcoded_edges])
            self.edges = hardcoded_edges
            self.M = M
        else:
            self.graph = GraphRandomizer(range(1, N + 1), M, False, force_edge_lim=False,
                                         base_attractibility=attractability)
            self.basis = basis
            self.edges = [(u, v, random_weight(basis)) for u, v in self.graph.edge_set]
            self.M = len(self.edges)

        self.Q = Q
        if hardcoded_queries is not None:
            assert isinstance(hardcoded_queries, list) and len(hardcoded_queries) == Q
            assert all([isinstance(q, tuple) and len(q) == 2 for q in hardcoded_queries])
            assert all([0 < q[0] <= N and 0 < q[1] <= N for q in hardcoded_queries])
            self.queries = hardcoded_queries
        else:
            self.queries = [(ra.randint(1, N), ra.randint(1, N)) for _ in range(Q)]


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
        TestCase(4, 3, 4, [], hardcoded_edges=[(1, 2, 5), (2, 3, 9), (3, 4, 33)],
                 hardcoded_queries=[(1, 3), (2, 4), (1, 4), (2, 3)]),
        TestCase(4, 4, 2, [], hardcoded_edges=[(1, 2, 5), (2, 3, 3), (3, 4, 6), (4, 1, 3)],
                 hardcoded_queries=[(1, 1), (2, 4)]),
        TestCase(5, 6, 4, [], hardcoded_edges=[(1, 2, 6), (2, 3, 4), (3, 4, 2), (4, 1, 5), (1, 3, 1), (4, 5, 4)],
                 hardcoded_queries=[(1, 3), (5, 4), (2, 1), (1, 1)])]
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
    UPPER_LIM = 10 ** 5

    stabilities = [10, 1, 5, 0, 100]

    def create_basis(size):
        assert 0 < size <= 59
        return [1 << p for p in random.sample(range(59), size)]

    basis_sizes = [4, 10, 59]

    graph_node_amt_limits = [10 ** 3, 10 ** 4, 10 ** 5]

    graph_edge_amt_funcs = [
        lambda N: min(5 * N // 4, N + 20, UPPER_LIM),
        lambda N: min(3 * N, UPPER_LIM),
        lambda N: min(N * (N - 1) // 2, UPPER_LIM)
    ]

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

    def node_limit_to_name(N):
        if N <= 10 ** 3:
            return 'few_nodes'
        if N <= 10 ** 4:
            return 'medium_nodes'
        return 'a_fuckton_of_nodes'

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
                    if not (len(batch) < 100 and N_remain >= 0 and M_remain >= 0):
                        break
                    batch.append(TestCase(N, M, node_lim, create_basis(basis_size), stability))
                make_secret_test(batch, 'main_{}_{}_{}'.format(node_limit_to_name(batch[0].N),
                                                               edge_node_ratio_to_name(batch[0].N, batch[0].M),
                                                               basis_size_to_name(basis_size)))

    # Make extra non-trivial stressed cases
    for s in stabilities:
        N = random.randint(9 * UPPER_LIM // 10, UPPER_LIM)
        M = min(UPPER_LIM, N + 5)
        basis_size = 59
        make_secret_test([TestCase(N, M, UPPER_LIM, create_basis(basis_size), s)], 'main_stressed')

    # Make some really dense graphs so it kills solutions where you calculate all cycles
    for s, i in zip(stabilities, range(5)):
        N = random.randint(900, 1000)
        M = UPPER_LIM
        basis_size = i + 3
        make_secret_test([TestCase(N, M, UPPER_LIM, create_basis(basis_size), s)], 'main_dense_graph')


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    
    TODO Implement this for your problem.
    """
    T = len(cases)
    assert T <= 100
    total_N, total_M, total_Q = 0, 0, 0
    print(T, file=file)
    for case in cases:
        assert case.N <= 10 ** 5 and case.M <= 10 ** 5 and case.Q <= 10 ** 5
        print(f'{case.N} {case.M} {case.Q}', file=file)
        total_N += case.N
        total_M += case.M
        total_Q += case.Q
        assert len(case.edges) == case.M
        for u, v, w in case.edges:
            assert 0 < u <= case.N and 0 < v <= case.N and 0 <= w <= 10 ** 18
            print(f'{u} {v} {w}', file=file)
        assert len(case.queries) == case.Q
        for u, v in case.queries:
            assert 0 < u <= case.N and 0 < v <= case.N
            print(f'{u} {v}', file=file)

    assert total_N <= 10 ** 5 and total_M <= 10 ** 5 and total_Q <= 10 ** 5


def solve(N: int, M: int, Q: int, U: list[int], V: list[int], W: list[int], A: list[int], B: list[int], file):
    nodes_xor = [0 for _ in range(N + 1)]
    graph = [[] for i in range(N + 1)]
    for i in range(M):
        graph[U[i]].append((V[i], W[i]))
        graph[V[i]].append((U[i], W[i]))

    dfs_tree = [[] for i in range(N + 1)]
    visited = set()
    basis = []

    def add_to_basis(x):
        for y in basis:
            x = min(x, y ^ x)
        if x != 0:
            basis.append(x)

    def dfs(u):
        visited.add(u)
        for v, w in graph[u]:
            if v not in visited:
                nodes_xor[v] = nodes_xor[u] ^ w
                dfs_tree[u].append(v)
                dfs(v)

    def triangles(u):
        for v in dfs_tree[u]:
            triangles(v)
        for v, w in graph[u]:
            add_to_basis(w ^ nodes_xor[u] ^ nodes_xor[v])

    dfs(1)
    triangles(1)

    for i in range(Q):
        answer = nodes_xor[A[i]] ^ nodes_xor[B[i]]
        for b in basis:
            answer = max(answer, answer ^ b)
        print(answer, file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    
    TODO Implement this for your problem by changing the import below.
    """
    for case in cases:
        N = case.N
        M = case.M
        Q = case.Q
        U = [edge[0] for edge in case.edges]
        V = [edge[1] for edge in case.edges]
        W = [edge[2] for edge in case.edges]
        A = [query[0] for query in case.queries]
        B = [query[1] for query in case.queries]
        solve(N, M, Q, U, V, W, A, B, file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
