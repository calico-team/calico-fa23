#pragma once
#include <bits/stdc++.h>
using namespace std;

#define dbg(x) cerr << x << endl

struct Graph {

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

    int V, E = 0;
    vector<vector<int>> adjList;
    vector<pair<int, int>> edgeList;
    vector<int> inDeg;
    vector<int> outDeg;
    set<pair<int, int>> edge_set;

    Graph(int _V) : V(_V), adjList(_V), inDeg(_V), outDeg(_V) {}

    void add_edge(int u, int v) {
        assert(u >= 0 && v >= 0);
        assert(u < V && v < V);
        if (edge_set.count({u, v})) return;
        adjList[u].push_back(v);
        edgeList.push_back({u, v});
        edge_set.insert({u,v});
        ++inDeg[v];
        ++outDeg[u];
        ++E;
    }

    long long stomachs_needed() {
        
        const long long INF = 1E9;
        Dinic mf(2 * V + 2);
        const int source = 2 * V, sink = 2 * V + 1;
        function<int(int)> in = [](int i) { return 2 * i; }, out = [](int i) { return 2 * i + 1; };

        for (int i = 0; i < V; ++i) {
            if (!inDeg[i]) mf.addEdge(source, in(i), INF);
            if (!outDeg[i]) mf.addEdge(out(i), sink, INF);
            mf.addEdge(in(i), out(i), (inDeg[i] && outDeg[i]) ? 1LL : INF);
            for (int j : adjList[i]) {
                mf.addEdge(out(i), in(j), INF);
            }
        }

        return mf.calc(source, sink);

    }

};

vector<int> generate_random_permutation(int N, mt19937_64& rng) {
    assert(N > 0);
    vector<int> p(N);
    iota(p.begin(), p.end(), 0);
    shuffle(p.begin(), p.end(), rng);
    return p;
}

Graph build_graph(int V, int E, mt19937_64& rng) {
    // dbg("Calculating permutation");
    vector<int> perm = generate_random_permutation(V, rng);
    Graph G(V);
    int sources = rng() % (V / 10) + 1;
    int sinks = rng() % (V / 10) + 1;
    // dbg("Generating random edges");
    // dbg("Connecting all sources");
    for (int i = 0; i < sources; ++i) {
        int u = sources + rng() % (V - sources - sinks);
        G.add_edge(perm[i], perm[u]);
    }
    // dbg("Connecting all middle nodes");
    for (int i = sources; i < V - sinks; ++i) {
        int source = rng() % sources;
        G.add_edge(perm[source], perm[i]);
        int sink = V - sinks + rng() % sinks;
        G.add_edge(perm[i], perm[sink]);
    }
    // dbg("Connecting all sinks");
    for (int i = V - sinks; i < V; ++i) {
        int u = sources + rng() % (V - sources - sinks);
        G.add_edge(perm[u], perm[i]);
    }
    while (G.E < E) {
        int u = rng() % V;
        int v = rng() % V;
        if (u == v) continue;
        if (u > v) swap(u, v);
        if (u < sources)
            if (v < sources || v >= V - sinks) continue;
        if (v >= V - sinks)
            if (u < sources || u >= V - sinks) continue;
        G.add_edge(perm[u], perm[v]);
    }
    return G;
}

Graph build_random_graph(int max_v, int max_e, mt19937_64& rng) {
    max_v = max_v / 2;
    int V = 9 * max_v / 10 + (rng() % max_v / 10);
    int E = 9 * max_e / 10 + (rng() % max_e / 10);
    return build_graph(V, E, rng);
}


Graph build_random_graph_one_articulation(int max_v, int max_e, mt19937_64& rng) {
    Graph G1 = build_random_graph(4 * max_v / 10, 4 * max_e / 10, rng);
    Graph G2 = build_random_graph(4 * max_v / 10, 4 * max_e / 10, rng);
    int N1 = G1.V, N2 = G2.V;
    Graph G(N1 + N2 + 1);
    vector<int> p = generate_random_permutation(N1 + N2 + 1, rng);
    for (auto& e : G1.edgeList) G.add_edge(p[e.first], p[e.second]);
    for (auto& e : G2.edgeList) G.add_edge(p[N1 + e.first], p[N1 + e.second]);
    for (int i = 0; i < N1; ++i) {
        if (!G1.outDeg[i]) {
            G.add_edge(p[i], p[N1 + N2]);
        }
    }
    for (int i = 0; i < N2; ++i) {
        if (!G2.inDeg[i]) {
            G.add_edge(p[N1 + N2], p[N1 + i]);
        }
    }
    return G;
}