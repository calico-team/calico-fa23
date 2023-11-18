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
 * U: the list of U_i for each portal
 * V: the list of V_i for each portal
 * W: the list of W_i for each portal
 * A: the list of A_i for each errand
 * B: the list of B_i for each errand
 * 
 */
void solve(int N, int M, int Q, vector<int>& U, vector<int>& V, vector<ll>& W, vector<int>& A, vector<int>& B) {

    vector<ll> nodes_xor(N + 1);
    vector<vector<pair<int,ll>>> g(N + 1);
    for (int i = 0; i < M; ++i) {
        g[U[i]].emplace_back(V[i], W[i]);
        g[V[i]].emplace_back(U[i], W[i]);
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
        ll answer = nodes_xor[A[i]] ^ nodes_xor[B[i]];
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
        vector<int> U(M), V(M), A(Q), B(Q);
        vector<ll> W(M);
        for (int j = 0; j < M; ++j) {
            cin >> U[j] >> V[j] >> W[j];
        }
        for (int j = 0; j < Q; ++j) {
            cin >> A[j] >> B[j];
        }
        solve(N, M, Q, U, V, W, A, B);
    }
}