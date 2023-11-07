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
SEED = 'hey it\'s lady gaga, I need $145 to continue working on my new song. ra ra ah ah ah'

from graph_randomizer import *

class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    
    TODO Change this to store the relevant information for your problem.
    """
    def __init__(self, B, F, N, M, force_lim= False, base_attractibility= None, incoming_attractibility= None, sink_attractability= None, edge_to_weight= lambda graph : lambda u, v : 1, XYK= None):
        if XYK is not None:
            self.B = B
            self.F = F
            self.N = N
            self.M = M
            self.X = XYK[0]
            self.Y = XYK[1]
            self.K = XYK[2]
            self.ready = True
            return

        self.N = N
        self.F = F
        self.ready = False

        self.graph = GraphRandomizer(range(1, N + 1), M, True, force_lim, base_attractibility, incoming_attractibility)
        self.M = len(self.graph.edge_set)
        self.graph.convert_to_dag(sink_attractability)

        self.X = []
        self.Y = []
        self.Z = []
        
        self.edge_to_weight = edge_to_weight
        self.weight_edges()

    def weight_edges(self):
        adj_ls = self.graph.make_adj_list()
        get_weight = self.edge_to_weight(adj_ls)

        for x, y in self.graph.edge_set:
            z = get_weight(x, y)
            self.X.append(x)
            self.Y.append(y)
            self.Z.append(z)
        
        self.ready = True
    
    def print_graph(self):
        assert self.ready
        for i in self.graph.node_list:
            print(i)
        
        for x, y, z in self.X, self.Y, self.Z:
            print(x, y, z)


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
    x1 = [1, 1, 2, 2, 3, 5, 3]
    y1 = [2, 3, 3, 4, 4, 4, 5]
    z1 = [1, 2, 2, 3, 4, 7, 1]

    x2 = [2, 2, 2, 4, 4, 1]
    y2 = [4, 1, 3, 1, 3, 3]
    z2 = [2, 2, 4, 1, 3, 4]

    x3 = [4, 4, 9, 3, 1, 5, 5, 6, 2, 8, 8]
    y3 = [3, 1, 6, 5, 5, 2, 8, 8, 7, 7, 10]
    z3 = [3, 1, 4, 9, 2, 3, 2, 2, 1, 4, 3]

    main_sample_cases = [
        TestCase(5, 7, XYZ= [x1, y1, z1]),
        TestCase(4, 6, XYZ= [x2, y2, z2]),
        TestCase(10, 11, XYZ= [x3, y3, z3]),
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
    CEIL = 10 ** 3
    FLOOR = 1

    def safe_gauss(mu, sig):
        return int(max(min(ra.gauss(mu, sig), CEIL), FLOOR))
    
    def rev_adj_list(adj_ls):
        new_adj_ls = {x : [] for x in adj_ls}
        for x in adj_ls:
            for y in adj_ls[x]:
                new_adj_ls[y].append(x)
        return new_adj_ls

    def make_deeper_heavier_dist(sig, damp, inv= False):
        assert 0 < damp <= 1

        def deeper_heavier(adj_ls):
            reversed = rev_adj_list(adj_ls)

            min_depth_from_source = {}

            from collections import deque
            q = deque([])
            seen = set()
            for x in reversed:
                if len(reversed[x]) == 0:
                    q.append((x, 0))
                    seen.add(x)
            
            deepest = 0
            while len(q) > 0:
                x, d = q.popleft()
                min_depth_from_source[x] = d
                for y in adj_ls[x]:
                    if y not in seen:
                        deepest = max(deepest, d + 1)

                        q.append((y, d + 1))
                        seen.add(y)
            
            assert len(min_depth_from_source) == len(adj_ls), "{}\n{}".format(adj_ls, min_depth_from_source)

            def w(u, v):
                depth = max(min_depth_from_source[u], min_depth_from_source[v])
                factor = depth / deepest # alternatively, can divide by sum of depths
                assert 0 < factor <= 1
                return safe_gauss((factor if not inv else (1 - factor)) * CEIL * damp, sig)

            return w
        
        return deeper_heavier
    
    make_secret_test([
        TestCase(5, 12, edge_to_weight= make_deeper_heavier_dist(3, 25 / 1000)),
        TestCase(24, 60, edge_to_weight= make_deeper_heavier_dist(3, 25 / 1000)),
        TestCase(24, 40, edge_to_weight= make_deeper_heavier_dist(2, 10 / 1000)),
    ], 'main_small_uniform')

    make_secret_test([
        TestCase(5, 4, edge_to_weight= make_deeper_heavier_dist(3, 25 / 1000)),
        TestCase(24, 23, edge_to_weight= make_deeper_heavier_dist(3, 25 / 1000)),
        TestCase(24, 23, edge_to_weight= make_deeper_heavier_dist(2, 10 / 1000)),
    ], 'main_small_trees')

    sigs = [0, 1, 3, 5, 10, 50, 100, 250]
    damps = [x / 1000 for x in [5, 10, 25, 50, 100, 250, 500, 1000]]

    fuzz_trees_tests = []
    for d in damps:
        for s in sigs:
            if s > d / 2:
                continue
            fuzz_trees_tests.append(TestCase(1000, 999, edge_to_weight= make_deeper_heavier_dist(s, d)))
            fuzz_trees_tests.append(TestCase(1000, 999, edge_to_weight= make_deeper_heavier_dist(s, d, inv= True)))

    make_secret_test(fuzz_trees_tests, 'main_tree_fuzz')

    degree_factor = [1.0, 1.25, 2.5, 5.5, 10.5]
    degree_factor_reduced = [1.0, 1.25, 10.5, 50.5]
    node_values_low = [10, 25, 50]
    node_values_med = [125] #, 250]
    # node_values_high = [500, 1000]

    fuzz_dag_tests = []
    for d in damps:
        for s in sigs:
            if s > d / 2 or e() < 0.5:
                continue
            for n in node_values_low:
                for df in degree_factor:
                    if df > n:
                        continue
                    fuzz_dag_tests.append(TestCase(n, int(n * df), edge_to_weight= make_deeper_heavier_dist(s, d)))
                    fuzz_dag_tests.append(TestCase(n, int(n * df), edge_to_weight= make_deeper_heavier_dist(s, d, inv= True)))

    make_secret_test(fuzz_dag_tests, 'main_dag_fuzz_small')

    fuzz_dag_tests = []
    for d in damps:
        for s in sigs:
            if s > d / 2 or e() < 0.5:
                continue
            for n in node_values_med:
                for df in degree_factor_reduced:
                    if df > n:
                        continue
                    fuzz_dag_tests.append(TestCase(n, int(n * df), edge_to_weight= make_deeper_heavier_dist(s, d)))
                    fuzz_dag_tests.append(TestCase(n, int(n * df), edge_to_weight= make_deeper_heavier_dist(s, d, inv= True)))

    make_secret_test(fuzz_dag_tests, 'main_dag_fuzz_med')

    make_secret_test([TestCase(5000, 10000, edge_to_weight= make_deeper_heavier_dist(20, 100 / 1000))], 'main_dag_stress')
    make_secret_test([TestCase(5000, 10000, edge_to_weight= make_deeper_heavier_dist(20, 100 / 1000, inv= True))], 'main_dag_stress_inv')
    make_secret_test([TestCase(10000, 10000 - 1, edge_to_weight= make_deeper_heavier_dist(20, 100 / 1000))], 'main_tree_stress')
    make_secret_test([TestCase(10000, 10000 - 1, edge_to_weight= make_deeper_heavier_dist(20, 100 / 1000, inv= True))], 'main_tree_stress_inv')

    # TODO: nonuniform attractibility values




def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    
    TODO Implement this for your problem.
    """
    T = len(cases)
    print(T, file=file)
    total_N = 0
    total_M = 0
    total_T = 0
    for case in cases:
        assert case.ready
        assert len(case.X) == len(case.Y) == len(case.Z) == case.M, "X:{}:Y:{}:Z:{}:M:{}".format(len(case.X), len(case.Y), len(case.Z), case.M)

        print(case.F, case.B, file=file)
        print(case.N, case.M, case.S, case.E, file=file)
        assert(case.S != case.E)
        total_T += 1
        total_N += case.N
        total_M += case.M

        print(total_T)

        assert total_T <= 100
        assert total_N <= 10 ** 5 and total_M <= 10 ** 5, "T:{}:TN:{}:TM:{}".format(total_T, total_N, total_M)
        
        print(*case.K)
        for k in case.K:
            assert(k != case.S and k != case.E and 1 <= k <= case.N)

        edges_zero_indexed = []
        for x, y in zip(case.X, case.Y):
            edges_zero_indexed.append((x - 1, y - 1))
            print(x, y, file=file)

        from dag_check import Graph, isConnected
        assert isConnected(Graph(edges_zero_indexed, case.N), case.N)


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
        print(solve(case.F, case.B, case.N, case.M, case.S, case.E, case.X, case.Y, case.K), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()