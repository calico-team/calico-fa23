#include <iostream>
#include <vector>
#include <queue>
using namespace std;

/**
 * Print in the first line the number K of computers Bessie the Cow should eat.
 * Print in the next line K numbers, one for each different computer she should eat.
 * If her task is not possible, print "IMPOSSIBLE"
 * 
 * N: Number of computers.
 * M: Number of connections between computers.
 * S: Number of stomachs.
 * U: Initial computer for each of the M connections.
 * V: Final computer for each of the M connections.
 * 
*/
void solve(int N, int M, int S, vector<int>& U, vector<int>& V) {
    // Solution is an articulation point which is neither a contestant nor judgehost.
    vector<vector<int>> adj(N + 1);
    vector<bool> contestants(N + 1, true), judgehosts(N + 1, true);
    for (int i = 0; i < M; ++i) {
        adj[U[i]].push_back(V[i]);
        contestants[V[i]] = false;
        judgehosts[U[i]] = false;
    }
    vector<bool> visited(N + 1, false);
    queue<int> q;
    for (int i = 1; i <= N; ++i)
        if (contestants[i])
            q.push(i), visited[i] = true;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        if (q.empty() && !contestants[u] && !judgehosts[u]) {
            cout << "1\n";
            cout << u << '\n';
            return;
        }
        for (int v : adj[u])
            if (!visited[v])
                visited[v] = true, q.push(v);
    }
    cout << "IMPOSSIBLE\n";
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        int N, M, S;
        cin >> N >> M >> S;
        vector<int> U(M), V(M);
        for (int j = 0; j < M; ++j) {
            cin >> U[j] >> V[j];
        }
        solve(N, M, S, U, V);
    }
    return 0;
}