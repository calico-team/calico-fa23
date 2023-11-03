#include <bits/stdc++.h>
using namespace std;

/**
 * Bessie the Cow can only ruin CALICO if there is a point in
 * time where only one computer has submissions that have to be sent, as she
 * only has 1 stomach.
 * We can turn the next computers from a contestant into "fake contestants",
 * since they also have submissions to be judged.
 * 
 * This behaviour is the same as running a multi-source BFS from each contestant,
 * and check if the queue is empty at any point. The idea is the same as a topological sort.
 * 
 * Time complexity: O(N + M)
*/
void bfs_solution(int N, int M, int S, vector<int>& U, vector<int>& V) {
    vector<vector<int>> adj(N + 1);
    // Add edges to the graph
    for (int i = 0; i < M; ++i) {
        adj[U[i]].push_back(V[i]);
    }
    // Check which computers are judges
    vector<bool> is_judge(N + 1, true);
    for (int i = 0; i < M; ++i) {
        is_judge[U[i]] = false;
    }
    // Add one "super judge" at index 0
    for (int i = 1; i <= N; ++i) {
        if (is_judge[i]) {
            adj[i].push_back(0);
        }
    }
    // Check which computers are contestants and add them to the BFS queue
    queue<int> contestants;
    vector<bool> is_contestant(N + 1, true);
    vector<bool> is_initial_contestant(N + 1, true);
    is_contestant[0] = is_initial_contestant[0] = false;
    for (int i = 0; i < M; ++i) {
        is_contestant[V[i]] = is_initial_contestant[V[i]] = false;
    }
    for (int i = 0; i <= N; ++i) {
        if (is_contestant[i]) {
            contestants.push(i);
        }
    }
    
    // Run algorithm:
    
    while (!contestants.empty()) {
        int contestant = contestants.front();
        contestants.pop();
        if (contestants.empty()) {
            // Bessie can't eat imaginary computers (yet), judgehosts or contestant computers.
            if (contestant != 0 && !is_judge[contestant] && !is_initial_contestant[contestant]) {
                // It's a solution
                cout << contestant << '\n';
                return;
            }
        }

        for (int computer : adj[contestant]) {
            // Try to turn it into a "fake contestant":
            if (!is_contestant[computer]) {
                is_contestant[computer] = true;
                contestants.push(computer);
            }
        }
    }
    cout << "IMPOSSIBLE\n";
}



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
        for (int L = 0; L < 31; ++L) do { // 'int L=30' maybe faster for random data
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
 * Bessie the Cow will be able to eat enough computers with her S stomachs if
 * we can take out a number S' <= S of nodes in the connectivity graph such that
 * no contestant is able to reach a judge host.
 * 
 * This number S' can be calculated with a flow graph, adding a source node that connects to
 * every contestant, a sink node that will be connected to every judge host and duplicating
 * each computer, adding a flow of 1 in between. The maximum flow of the graph 
 * from the source to the sink is precisely S'.
 * 
 * We can do this using a maxflow algorithm such as Dinic.
 * 
 * Time complexity: O((M + N)√N) (the flow graph is bipartite since we are duplicating the nodes)
*/
void mincut_solution(int N, int M, int S, vector<int>& U, vector<int>& V) {

    Dinic flow(2 * N + 2);
    // flow.init(2 * N + 2);
    const int source = 0, sink = 1;
    // These lambda expressions are so the code below is more readable.
    auto in = [](int i) { return 2 * i; };
    auto out = [](int i) { return 2 * i + 1; };
    // S + 1 is a good "infinity" in the sense that if the answer is bigger than that, we return false.
    const int INF = S + 1; 
    // Check which computers are contestants and which are judges.
    vector<bool> is_contestant(N + 1, true);
    vector<bool> is_judge(N + 1, true);
    is_contestant[0] = is_judge[0] = false;
    for (int i = 0; i < M; ++i) {
        is_contestant[V[i]] = false;
        is_judge[U[i]] = false;
    }
    // Connect source to contestants.
    for (int i = 1; i <= N; ++i) {
        if (is_contestant[i]) {
            flow.addEdge(source, in(i), INF);
        }
    }
    // Connect judges to sink
    for (int i = 1; i <= N; ++i) {
        if (is_judge[i]) {
            flow.addEdge(out(i), sink, INF);
        }
    }
    // Duplicate nodes
    for (int i = 1; i <= N; ++i) {
        // Bessie can't eat contestants nor judgehosts
        if (!is_contestant[i] && !is_judge[i]) {
            flow.addEdge(in(i), out(i), 1);
        } else {
            flow.addEdge(in(i), out(i), INF);
        }
    }
    // Add edges
    for (int i = 0; i < M; ++i) {
        flow.addEdge(out(U[i]), in(V[i]), INF);
    }

    // Calculate S'
    int S_ = flow.calc(source, sink);
    // If S' > S, there aren't enough stomachs
    if (S_ > S) {
        cout << "IMPOSSIBLE\n";
    } else {
        // For each node, check if the input and the output are in different parts of the mincut
        for (int i = 1; i <= N; ++i) {
            if (flow.leftOfMinCut(in(i)) ^ flow.leftOfMinCut(out(i))) {
                cout << i << ' ';
            }
        }
        cout << '\n';
    }

}


/**
 * 
 * N: Number of computers.
 * M: Number of connections between computers.
 * S: Number of stomachs.
 * U: Initial computer for each of the M connections.
 * V: Final computer for each of the M connections.
 * 
*/
void solve(int N, int M, int S, vector<int>& U, vector<int>& V) {
    // YOUR CODE HERE
    if (S == 1) {
        bfs_solution(N, M, S, U, V);
    } else {
        mincut_solution(N, M, S, U, V);
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