#include <bits/stdc++.h>
using namespace std;

using ll = long long;

/**
 * Output Q lines, where the i-th line contains the maximum
 * fuel charge possible for the i-th errand
 *     
 * N: the number of universes
 * M: the number of portals
 * Q: the number of queries
 * U: the list containing U_i for each query
 * V: the list containing V_i for each query
 * A: the list of A_i for each portal
 * B: the list of B_i for each portal
 * C: the list of fuel charges for each portal
 * 
 */
void solve(int N, int M, int Q, vector<int>& U, vector<int>& V, vector<int>& A, vector<int>& B, vector<ll>& C) {

    vector<ll> nodes_xor(N + 1);
    vector<vector<pair<int,ll>>> g(N + 1);
    for (int i = 0; i < M; ++i) {
        g[A[i]].emplace_back(B[i], C[i]);
        g[B[i]].emplace_back(A[i], C[i]);
    }

    vector<vector<int>> dfs_tree(N + 1);
    vector<bool> visited(N + 1, false);
    vector<ll> basis;

    function<void(ll)> add_to_basis = [&](ll x) {
        for (ll y : basis) x = min(x, y ^ x);
        if (x) basis.push_back(x);
    };

    // Create DFS tree
    function<void(int)> dfs = [&](int u) {
        visited[u] = true;
        for (auto& [v, w] : g[u]) {
            if (!visited[v]) {
                nodes_xor[v] = nodes_xor[u] ^ w;
                dfs_tree[u].push_back(v);
                dfs(v);
            }
        }
    };

    function<void(int)> triangles = [&](int u) {
        for (int v : dfs_tree[u]) triangles(v);
        for (auto& [v, w] : g[u]) {
            // Triange 1 -> u -> v
            add_to_basis(w ^ nodes_xor[u] ^ nodes_xor[v]);
        }
    };

    dfs(1);
    triangles(1);

    for (int i = 0; i < Q; ++i) {
        ll answer = nodes_xor[U[i]] ^ nodes_xor[V[i]];
        for (ll b : basis) answer = max(answer, answer ^ b);
        cout << answer << '\n';
    }

}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, M, Q;
        cin >> N >> M >> Q;
        vector<int> A(M);
        vector<int> B(M);
        vector<ll> C(M);
        for (int j = 0; j < M; j++) {
            cin >> A[j] >> B[j] >> C[j];
        }
        vector<int> U(Q), V(Q);
        for (int j = 0; j < Q; ++j) {
            cin >> U[j] >> V[j];
        }
        solve(N, M, Q, U, V, A, B, C);
    }
}