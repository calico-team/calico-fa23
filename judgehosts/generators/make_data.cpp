#include <bits/stdc++.h>
#include "calico_lib.cpp"
#include "solution.cpp"
#include "graph_generator.cpp"
using namespace std;

#define NUMBER_OF_TEST_CASES 1
#define UNLIMITED_TEST_CASES 2 // Use this for problems with just one test case too.
#define SENTINEL_CASE 3

const int _TYPE_OF_OUTPUT_ = NUMBER_OF_TEST_CASES; // CHANGE THIS ACCORDING TO THE TYPE OF PROBLEM
const string SENTINEL = "";

long long SEED = 33;
mt19937_64 rng;

struct TestCase {

    int N, M, S;
    vector<int> U, V;

    TestCase() {

    }

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
        if (int(U.size()) != M) return false;
        if (int(V.size()) != M) return false;
        if (N <= 0) return false;
        for (int ui : U) if (ui <= 0 || ui > N) return false;
        for (int vi : V) if (vi <= 0 || vi > N) return false;
        for (int i = 0; i < M; ++i) if (U[i] == V[i]) return false;
        // Check if it is a DAG
        TopoSort topo; topo.init(N + 1);
        for (int i = 0; i < M; ++i) topo.ae(U[i], V[i]);
        if (!topo.sort()) return false;
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
        if (!tc.isCorrect()) return false;
    }

    return total_N <= 1e3 && total_M <= 1e3;

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
        if (!tc.isCorrect()) return false;
        if (!tc.S != 1) return false;
        total_N += tc.N;
        total_M += tc.M;
    }
    return total_N <= 1e6 && total_M <= 1e6;
}

bool is_correct_bonus_b_case(vector<TestCase> const& v) {
    // A bonus test case is correct if the sum for values of N and M in the case of S=1 is less or equal than 1e6
    // and the values for N and M in the case S > 1 is less or equal than 1e4
    int total_N = 0, total_M = 0;
    for (auto& tc : v) {
        if (!tc.isCorrect()) return false;
        if (!tc.S != 1) return false;
        total_N += tc.N;
        total_M += tc.M;
    }
    return total_N <= 1e4 && total_M <= 1e4;
}

inline ostream& operator << (ostream& out, TestCase const& tc) {
    // Implement this operator with how you want your test case to be shown in the input
    out << tc.N << ' ' << tc.M << ' ' << tc.S << '\n';
    for (int i = 0; i < tc.M - 1; ++i) cout << tc.U[i] << ' ';
    if (tc.M) cout << tc.U.back();
    cout << '\n';
    for (int i = 0; i < tc.M - 1; ++i) cout << tc.V[i] << ' ';
    if (tc.M) cout << tc.V.back();
}

void make_sample_tests() {
    vector<TestCase> main_sample_cases = {
        // TODO : Fill in with main sample cases
    };
    assert(is_correct_main_case(main_sample_cases));
    make_sample_test(main_sample_cases, "main");
    
    vector<TestCase> bonus_a_sample_cases = {
        // TODO : Fill in with bonus sample cases
    };
    assert(is_correct_bonus_a_case(bonus_a_sample_cases));
    make_sample_test(bonus_a_sample_cases, "bonus_a");

    vector<TestCase> bonus_b_sample_cases = {
        // TODO : Fill in with bonus sample cases
    }
    assert(is_correct_bonus_b_case(bonus_b_sample_cases));
    make_sample_test(bonus_b_sample_cases, "bonus_b");
}

void make_secret_tests() {

    // Test cases for main

    for (int i = 0; i < 10; ++i) {
        // Small multiple cases
        vector<TestCase> main_secret_multiple_random;
        for (int i = 0; i < 5; ++i) {
            Graph G = (rng() % 2) ? build_random_graph(200, 200, rng) : build_random_graph_one_articulation(200, 200, rng);
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
        make_secret_test(main_secret_one_random, "main_single")
    }

    // Test cases for bonus A

    for (int i = 0; i < 10; ++i) {
        // Small multiple cases
        vector<TestCase> bonus_a_secret_multiple_random;
        for (int i = 0; i < 5; ++i) {
            Graph G = (rng() % 2) ? build_random_graph(200000, 200000, rng) : build_random_graph_one_articulation(200000, 200000, rng);
            TestCase tc;
            tc.importGraph(G);
            tc.S = 1;
            main_secret_multiple_random.push_back(tc);
        }
        assert(is_correct_main_case(bonus_a_secret_multiple_random));
        make_secret_test(bonus_a_secret_multiple_random, "bonus_a_multiple");
        // One big case
        vector<TestCase> bonus_a_secret_one_random;
        Graph G = (rng() % 2) ? build_random_graph(1000000, 1000000, rng) : build_random_graph_one_articulation(1000000, 1000000, rng);
        TestCase tc;
        tc.importGraph(G);
        tc.S = 1;
        bonus_a_secret_one_random.push_back(tc);
        assert(is_correct_main_case(bonus_a_secret_one_random));
        make_secret_test(bonus_a_secret_one_random, "bonus_a_single")
    }

    // Test cases for bonus B

    for (int i = 0; i < 10; ++i) {
        // Small multiple cases
        vector<TestCase> bonus_b_secret_multiple_random;
        for (int i = 0; i < 5; ++i) {
            Graph G = build_random_graph(2000, 2000, rng);
            TestCase tc;
            tc.importGraph(G);
            tc.S = max(G.stomachs_needed() - rng() % 2);
            main_secret_multiple_random.push_back(tc);
        }
        assert(is_correct_main_case(bonus_b_secret_multiple_random));
        make_secret_test(bonus_b_secret_multiple_random, "bonus_b_multiple");
        // One big case
        vector<TestCase> bonus_b_secret_one_random;
        Graph G = build_random_graph(10000, 10000, rng);
        TestCase tc;
        tc.importGraph(G);
        tc.S = max(G.stomachs_needed() - rng() % 2);
        bonus_b_secret_one_random.push_back(tc);
        assert(is_correct_main_case(bonus_b_secret_one_random));
        make_secret_test(bonus_b_secret_one_random, "bonus_b_single")
    }
    
    // Make edge cases???

        

}

void make_test_in(vector<TestCase>& cases, fstream& file) {
    // Leave this as it is. Do not touch it with your dirty hands...
    if (_TYPE_OF_OUTPUT_ == NUMBER_OF_TEST_CASES) {
        file << int(cases.size()) << '\n';
    }
    for (auto& tc : cases) file << tc << '\n';
    if (_TYPE_OF_OUTPUT_ == SENTINEL_CASE) {
        file << SENTINEL << '\n';
    }
}

void make_test_out(vector<TestCase>& cases, fstream& file) {
    for (TestCase& tc : cases) {
        solve(tc.N, tc.M, tc.S, tc.U, tc.V, file);
    }
}

int main() {
    make_data(make_sample_tests, make_secret_tests, make_test_in, make_test_out, SEED, rng);
}