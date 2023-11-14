#include <bits/stdc++.h>
#include "calico_lib.cpp"
#include "solution.cpp"
#include "graph_generator.cpp"
#include "greedy_algorithm.cpp"
using namespace std;

#define NUMBER_OF_TEST_CASES 1
#define UNLIMITED_TEST_CASES 2 // Use this for problems with just one test case too.
#define SENTINEL_CASE 3

const int _TYPE_OF_OUTPUT_ = NUMBER_OF_TEST_CASES; // CHANGE THIS ACCORDING TO THE TYPE OF PROBLEM
const string SENTINEL = "";

long long SEED = 33;
mt19937_64 rng;

const int MAIN_MAXN = 1E3;
const int A_MAXN = 5e5;
const int B_MAXN = 1e4;
const int C_MAXN = 5e5;

struct TestCase {

    int N, M, S;
    vector<int> U, V;

    TestCase() {}

    TestCase(int N, int M, int S, vector<int> U, vector<int> V) : N(N), M(M), S(S), U(U), V(V) {}

    void importGraph(Graph const& G) {
        N = G.V, M = G.E;
        for (auto& e : G.edgeList) {
            U.push_back(e.first + 1);
            V.push_back(e.second + 1);
        }
    }

    struct TopoSort {
        int N; vector<int> in, res;
        vector<vector<int>> adj;
        void init(int _N) { N = _N; in.resize(N); adj.resize(N); }
        void ae(int x, int y) { adj[x].push_back(y), ++in[y]; }
        bool sort() {
            queue<int> todo; 
            for (int i = 0; i < N; ++i) if (!in[i]) todo.push(i);
            while (!todo.empty()) {
                int x = todo.front(); todo.pop(); res.push_back(x);
                for(int i : adj[x]) if (!(--in[i])) todo.push(i);
            }
            return int(res.size()) == N;
        }
    };

    /**
     * Check internal logic of the test case
    */
    bool isCorrect() const {
        // Check internal logic of the test case
        if (int(U.size()) != M) { dbg("Wrong U"); return false; }
        if (int(V.size()) != M) { dbg("Wrong V"); return false; }
        if (N <= 0) { dbg("Negative N"); return false; }
        for (int ui : U) if (ui <= 0 || ui > N) { dbg("ui out of bounds"); return false; }
        for (int vi : V) if (vi <= 0 || vi > N) { dbg("vi out of bounds"); return false; }
        for (int i = 0; i < M; ++i) if (U[i] == V[i]) { dbg("ui = vi"); return false; }
        // Check if it is a DAG
        TopoSort topo; topo.init(N + 1);
        for (int i = 0; i < M; ++i) topo.ae(U[i], V[i]);
        if (!topo.sort()) { dbg("Not a DAG"); return false; }
        return true;
    }
};

/**
 * Fill in with main test case restrictions.
 * Check for both restrictions on each test case and restrictions for the whole batch.
*/
bool is_correct_main_case(vector<TestCase> const& v) {

    // A main case is correct if every test case is correct and the sum of all values of N and M are less or equal than 1e6.

    int total_N = 0, total_M = 0;
    for (auto& tc : v) {
        total_N += tc.N;
        total_M += tc.M;
        if (!tc.isCorrect()) {
            dbg("Single wrong tc");
            return false;
        }
        if (tc.S != 1) return false;
    }

    return total_N <= MAIN_MAXN && total_M <= MAIN_MAXN;

}

/**
 * Fill in with bonus test case restrictions.
 * Check for both restrictions on each test case and restrictions for the whole batch.
*/
bool is_correct_bonus_a_case(vector<TestCase> const& v) {
    // A bonus test case is correct if the sum for values of N and M in the case of S=1 is less or equal than 1e6
    // and the values for N and M in the case S > 1 is less or equal than 1e4
    int total_N = 0, total_M = 0;
    for (auto& tc : v) {
        if (!tc.isCorrect()) { dbg("Single wrong tc in A"); return false; }
        if (tc.S != 1) { dbg("S is not 1 in A"); return false; }
        total_N += tc.N;
        total_M += tc.M;
    }
    if (total_N > A_MAXN) dbg("Too many nodes for A");
    if (total_M > A_MAXN) dbg("Too many edges for A");
    return total_N <= A_MAXN && total_M <= A_MAXN;
}

bool is_correct_bonus_b_case(vector<TestCase> const& v) {
    // A bonus test case is correct if the sum for values of N and M in the case of S=1 is less or equal than 1e6
    // and the values for N and M in the case S > 1 is less or equal than 1e4
    int total_N = 0, total_M = 0;
    for (auto& tc : v) {
        if (!tc.isCorrect()) { dbg("Single wrong tc in B"); return false; }
        total_N += tc.N;
        total_M += tc.M;
    }
    if (total_N > B_MAXN) dbg("Too many nodes for B");
    if (total_M > B_MAXN) dbg("Too many edges for B");
    return total_N <= B_MAXN && total_M <= B_MAXN;
}

bool is_correct_bonus_c_case(vector<TestCase> const& v) {
    // A bonus test case is correct if the sum for values of N and M in the case of S=1 is less or equal than 1e6
    // and the values for N and M in the case S > 1 is less or equal than 1e4
    int total_N = 0, total_M = 0;
    for (auto& tc : v) {
        if (!tc.isCorrect()) { dbg("Single wrong tc in C"); return false; }
        total_N += tc.N;
        total_M += tc.M;
    }
    if (total_N > C_MAXN) dbg("Too many nodes for C");
    if (total_M > C_MAXN) dbg("Too many edges for C");
    return total_N <= C_MAXN && total_M <= C_MAXN;
}

inline ostream& operator << (ostream& out, TestCase const& tc) {
    // Implement this operator with how you want your test case to be shown in the input
    out << tc.N << ' ' << tc.M << ' ' << tc.S << '\n';
    for (int i = 0; i < tc.M - 1; ++i) out << tc.U[i] << ' ' << tc.V[i] << '\n';
    if (tc.M) out << tc.U.back() << ' ' << tc.V.back();
    return out;
}

void make_sample_tests() {
    vector<TestCase> main_sample_cases = {
        TestCase(7, 8, 1, {5,7,7,1,1,2,3,3}, {1,1,2,2,3,4,4,6}),
        TestCase(5, 4, 1, {1,2,3,3}, {3,3,4,5}),
        TestCase(9, 10, 1, {1,2,2,2,8,4,6,3,9,9},{6,6,3,4,4,3,3,9,5,7})
    };
    assert(is_correct_main_case(main_sample_cases));
    make_sample_test(main_sample_cases, "main");
    
    vector<TestCase> bonus_a_sample_cases = {
        TestCase(7, 8, 1, {5,7,7,1,1,2,3,3}, {1,1,2,2,3,4,4,6}),
        TestCase(5, 4, 1, {1,2,3,3}, {3,3,4,5}),
        TestCase(9, 10, 1, {1,2,2,2,8,4,6,3,9,9},{6,6,3,4,4,3,3,9,5,7})
    };
    assert(is_correct_bonus_a_case(bonus_a_sample_cases));
    make_sample_test(bonus_a_sample_cases, "bonus_a");

    vector<TestCase> bonus_b_sample_cases = {
        TestCase(7, 8, 2, {5,7,7,1,1,2,3,3}, {1,1,2,2,3,4,4,6}),
        TestCase(4, 4, 2, {1,1,2,3}, {2,3,4,4})
    };
    assert(is_correct_bonus_b_case(bonus_b_sample_cases));
    make_sample_test(bonus_b_sample_cases, "bonus_b");
}

void make_secret_tests() {

    // Test cases for main

    dbg("Generating random main");

    for (int i = 0; i < 10; ++i) {
        // Small multiple cases
        vector<TestCase> main_secret_multiple_random;
        for (int i = 0; i < 5; ++i) {
            Graph G = (rng() % 2) ? build_random_graph(200, 200, rng) : build_random_graph_one_articulation(200, 200, rng);
            cerr << "Graph built!" << endl;
            TestCase tc;
            tc.importGraph(G);
            tc.S = 1;
            main_secret_multiple_random.push_back(tc);
        }
        assert(is_correct_main_case(main_secret_multiple_random));
        make_secret_test(main_secret_multiple_random, "main_multiple");
        // One big case
        vector<TestCase> main_secret_one_random;
        Graph G = (rng() % 2) ? build_random_graph(1000, 1000, rng) : build_random_graph_one_articulation(1000, 1000, rng);
        TestCase tc;
        tc.importGraph(G);
        tc.S = 1;
        main_secret_one_random.push_back(tc);
        assert(is_correct_main_case(main_secret_one_random));
        make_secret_test(main_secret_one_random, "main_single");
    }

    // Test cases for bonus A

    dbg("Generating random A");

    for (int i = 0; i < 5; ++i) {
        // Small multiple cases
        vector<TestCase> bonus_a_secret_multiple_random;
        for (int i = 0; i < 5; ++i) {
            Graph G = (rng() % 2) ? build_random_graph(A_MAXN / 5, A_MAXN / 5, rng) : build_random_graph_one_articulation(A_MAXN / 5, A_MAXN / 5, rng);
            TestCase tc;
            tc.importGraph(G);
            tc.S = 1;
            bonus_a_secret_multiple_random.push_back(tc);
        }
        assert(is_correct_bonus_a_case(bonus_a_secret_multiple_random));
        make_secret_test(bonus_a_secret_multiple_random, "bonus_a_multiple");
        // One big case
        vector<TestCase> bonus_a_secret_one_random;
        Graph G = (rng() % 2) ? build_random_graph(A_MAXN, A_MAXN, rng) : build_random_graph_one_articulation(A_MAXN, A_MAXN, rng);
        TestCase tc;
        tc.importGraph(G);
        tc.S = 1;
        bonus_a_secret_one_random.push_back(tc);
        assert(is_correct_bonus_a_case(bonus_a_secret_one_random));
        make_secret_test(bonus_a_secret_one_random, "bonus_a_single");
    }

    // Edge cases for A

    for (int i = 0; i < 5; ++i) {
        vector<TestCase> edge_cases;
        Graph G = build_random_graph(A_MAXN / 3, A_MAXN / 2, rng);
        Graph extended_G(G.V + 2);
        for (auto edge : G.edgeList) extended_G.add_edge(edge.first, edge.second);
        for (int i = 0; i < G.V; ++i)
            if (!G.inDeg[i]) extended_G.add_edge(G.V, i);
        for (int i = 0; i < G.V; ++i) {
            if (!G.outDeg[i]) extended_G.add_edge(i, G.V + 1);
        }
        TestCase tc;
        tc.importGraph(extended_G);
        tc.S = 1;
        edge_cases.push_back(tc);
        assert(is_correct_bonus_a_case(edge_cases));
        make_secret_test(edge_cases, "bonus_a_edge");
    }

    // Test cases for bonus B

    dbg("Generating random B");

    for (int i = 0; i < 10; ++i) {
        // Small multiple cases
        vector<TestCase> bonus_b_secret_multiple_random;
        for (int i = 0; i < 5; ++i) {
            Graph G = build_random_graph(2000, 2000, rng);
            TestCase tc;
            tc.importGraph(G);
            tc.S = max(int(G.stomachs_needed() - rng() % 2), 0);
            bonus_b_secret_multiple_random.push_back(tc);
        }
        assert(is_correct_bonus_b_case(bonus_b_secret_multiple_random));
        make_secret_test(bonus_b_secret_multiple_random, "bonus_b_multiple");
        // One big case
        vector<TestCase> bonus_b_secret_one_random;
        Graph G = build_random_graph(10000, 10000, rng);
        TestCase tc;
        tc.importGraph(G);
        tc.S = max(int(G.stomachs_needed() - rng() % 2), 0);
        bonus_b_secret_one_random.push_back(tc);
        assert(is_correct_bonus_b_case(bonus_b_secret_one_random));
        make_secret_test(bonus_b_secret_one_random, "bonus_b_single");
    }

    // Test cases for bonus C

    dbg("Generating random C");

    for (int i = 0; i < 10; ++i) {
        // Small multiple cases
        vector<TestCase> bonus_c_secret_multiple_random;
        for (int i = 0; i < 5; ++i) {
            Graph G = build_random_graph(100000, 100000, rng);
            TestCase tc;
            tc.importGraph(G);
            tc.S = max(int(G.stomachs_needed() - rng() % 2), 0);
            bonus_c_secret_multiple_random.push_back(tc);
        }
        assert(is_correct_bonus_c_case(bonus_c_secret_multiple_random));
        make_secret_test(bonus_c_secret_multiple_random, "bonus_c_multiple");
        // One big case
        vector<TestCase> bonus_c_secret_one_random;
        Graph G = build_random_graph(500000, 500000, rng);
        TestCase tc;
        tc.importGraph(G);
        tc.S = max(int(G.stomachs_needed() - rng() % 2), 0);
        bonus_c_secret_one_random.push_back(tc);
        assert(is_correct_bonus_c_case(bonus_c_secret_one_random));
        make_secret_test(bonus_c_secret_one_random, "bonus_c_single");
    }    

}

void make_test_in(vector<TestCase>& cases, string const& path) {
    // Leave this as it is. Do not touch it with your dirty hands...
    freopen(path.c_str(), "w", stdout);
    if (_TYPE_OF_OUTPUT_ == NUMBER_OF_TEST_CASES) {
        cout << int(cases.size()) << '\n';
    }
    for (auto& tc : cases) cout << tc << '\n';
    if (_TYPE_OF_OUTPUT_ == SENTINEL_CASE) {
        cout << SENTINEL << '\n';
    }
}

void make_test_out(vector<TestCase>& cases, string const& path) {
    freopen(path.c_str(), "w", stdout);
    for (TestCase& tc : cases) {
        solve(tc.N, tc.M, tc.S, tc.U, tc.V);
    }
}

int main() {
    make_data(make_sample_tests, make_secret_tests, make_test_in, make_test_out, SEED, rng);
}