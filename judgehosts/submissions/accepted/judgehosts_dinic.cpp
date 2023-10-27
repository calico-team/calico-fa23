#include <iostream>
#include <vector>
#include <climits>
using namespace std;

/**
 * Description: Calculates maximum flow of a graph
 * Time: $O(N^2M)$ flow, $O(M\sqrt N)$ bipartite matching
 * Source: KACTL, https://github.com/kth-competitive-programming/kactl/blob/main/content/graph/Dinic.h
 */

struct Dinic {
    struct Edge {
        int to, rev;
        long long c, oc;
        long long flow() { return max(oc - c, 0LL); } // if you need flows
    };
    vector<int> lvl, ptr, q;
    vector<vector<Edge>> adj;
    Dinic(int n) : lvl(n), ptr(n), q(n), adj(n) {}
    void addEdge(int a, int b, long long c, long long rcap = 0) {
        adj[a].push_back({b, int(adj[b].size()), c, c});
        adj[b].push_back({a, int(adj[a].size()) - 1, rcap, rcap});
    }
    long long dfs(int v, int t, long long f) {
        if (v == t || !f) return f;
        for (int& i = ptr[v]; i < int(adj[v].size()); i++) {
            Edge& e = adj[v][i];
            if (lvl[e.to] == lvl[v] + 1)
                if (long long p = dfs(e.to, t, min(f, e.c))) {
                    e.c -= p, adj[e.to][e.rev].c += p;
                    return p;
                }
        }
        return 0;
    }
    long long calc(int s, int t) {
        long long flow = 0; q[0] = s;
        for (int L = 30; L < 31; ++L) do { // 'int L=30' maybe faster for random data
            lvl = ptr = vector<int>(int(q.size()));
            int qi = 0, qe = lvl[s] = 1;
            while (qi < qe && !lvl[t]) {
                int v = q[qi++];
                for (Edge e : adj[v])
                    if (!lvl[e.to] && e.c >> (30 - L))
                        q[qe++] = e.to, lvl[e.to] = lvl[v] + 1;
            }
            while (long long p = dfs(s, t, LLONG_MAX)) flow += p;
        } while (lvl[t]);
        return flow;
    }
    bool leftOfMinCut(int a) { return lvl[a] != 0; }
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
    Dinic flow(2 * N + 2);
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
        cout << int(computers_eaten.size()) << '\n';
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