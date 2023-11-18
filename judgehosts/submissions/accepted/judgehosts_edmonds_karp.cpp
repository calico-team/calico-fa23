#include <bits/stdc++.h>
using namespace std;

struct EdmondsKarp {

    int n;
    vector<unordered_map<int, int>> capacity;
    vector<vector<int>> adj;
    vector<bool> left;

    EdmondsKarp(int _n) : n(_n), capacity(_n), adj(_n), left(_n) {}

    void addEdge(int u, int v, int cap) {
        adj[u].push_back(v);
        adj[v].push_back(u);
        capacity[u][v] += cap;
    }

    int bfs(int s, int t, vector<int>& parent) {
        fill(parent.begin(), parent.end(), -1);
        parent[s] = -2;
        queue<pair<int, int>> q;
        q.push({s, 1E6});

        while (!q.empty()) {
            int cur = q.front().first;
            int flow = q.front().second;
            q.pop();

            for (int next : adj[cur]) {
                if (parent[next] == -1 && capacity[cur][next]) {
                    parent[next] = cur;
                    int new_flow = min(flow, capacity[cur][next]);
                    if (next == t)
                        return new_flow;
                    q.push({next, new_flow});
                }
            }
        }

        return 0;
    }

    int calc(int s, int t) {
        int flow = 0;
        vector<int> parent(n);
        int new_flow;

        while (new_flow = bfs(s, t, parent)) {
            flow += new_flow;
            int cur = t;
            while (cur != s) {
                int prev = parent[cur];
                capacity[prev][cur] -= new_flow;
                capacity[cur][prev] += new_flow;
                cur = prev;
            }
        }

        function<void(int)> dfs =  [&](int u) {
            left[u] = true;
            for (int v : adj[u]) if (capacity[u][v] > 0 && !left[v]) dfs(v);
        };

        dfs(s);

        return flow;

    }

    bool leftOfMinCut(int a) { return left[a]; }

};

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
    // Calculate the minimum vertex cut of the graph using Max Flow (Dinic).
    EdmondsKarp flow(2 * N + 2);
    int source = 0, sink = 1;
    auto in = [](int i) { return 2 * i; };
    auto out = [](int i) { return 2 * i + 1; };
    long long inf = S + 1;
    vector<bool> contestants(N + 1, true), judgehosts(N + 1, true);
    for (int i = 0; i < M; ++i) {
        contestants[V[i]] = false;
        judgehosts[U[i]] = false;
        flow.addEdge(out(U[i]), in(V[i]), inf);
    }
    for (int i = 1; i <= N; ++i) {
        if (contestants[i]) {
            flow.addEdge(source, in(i), inf);
            flow.addEdge(in(i), out(i), inf);
        } else if (judgehosts[i]) {
            flow.addEdge(out(i), sink, inf);
            flow.addEdge(in(i), out(i), inf);
        } else {
            flow.addEdge(in(i), out(i), 1);
        }
    }
    long long computers_needed = flow.calc(source, sink);
    if (computers_needed > S) {
        cout << "IMPOSSIBLE\n";
    } else {
        vector<int> computers_eaten;
        for (int i = 1; i <= N; ++i)
            if (flow.leftOfMinCut(in(i)) ^ flow.leftOfMinCut(out(i))) // One is on the left and the other is on the right
                computers_eaten.push_back(i);
        for (int i = 0; i < int(computers_eaten.size()) - 1; ++i)
            cout << computers_eaten[i] << ' ';
        if (!computers_eaten.empty())
            cout << computers_eaten.back();
        cout << '\n';
    }
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