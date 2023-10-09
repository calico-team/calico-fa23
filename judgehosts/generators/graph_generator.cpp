#pragma once
#include <bits/stdc++.h>
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

struct Graph {

    int V, E;
    vector<vector<int>> adjList;
    vector<pair<int, int>> edgeList;
    vector<int> inDeg;
    vector<int> outDeg;
    TopoSort topo;
    set<pair<int, int>> edge_set;

    Graph(int V) : V(V), inDeg(V, true), outDeg(V, true) {}

    void add_edge(int u, int v) {
        assert(u < V && v < V);
        adjList[u].push_back(v);
        edgeList.push_back({u, v});
        topo.ae(u, v);
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

    void elongatePaths() {
        // Make sure that all paths are of at least length 2
        topo.sort();
        vector<int>& toposort = topo.res;
        if (!edge_set.count({toposort[0], toposort[V / 2]})) {
            add_edge(toposort[0], toposort[V / 2]);
        }
        if (!edge_set.count({toposort[V / 2], toposort[V - 1]})) {
            add_edge(toposort[V / 2], toposort[V - 1]);
        }
        topo.sort();
        toposort = topo.res;
        vector<int> dp(V); // dp[u] = lenght of shortest path that ends in u

        for (int u : toposort) {
            for (int v : adjList[u]) {
                dp[v] = min(dp[u] + 1, dp[v]);
            }           
        }

        for (int u : toposort) {
            if (!outDeg[u]) {
                if (dp[u] < 2) { // this might work i guess
                    if (!edge_set.count({toposort[0], u})) add_edge(toposort[0], u);
                    if (!edge_set.count({u, toposort[V - 1]})) add_edge(u, toposort[V - 1]);
                    dp[toposort.back()] = 2; // lets not try to mess this up xdd
                }
            }
        }

    }

};

vector<int> generate_random_permutation(int N, mt19937_64& rng) {
    vector<int> p(N);
    iota(p.begin(), p.end(), 0);
    for (int i = 0; i < N; ++i) {
        int j = rng() % N;
        swap(p[i], p[j]);
    }
}

vector<long long> generate_random_subset(long long maxN, int sz, mt19937_64& rng) {
    vector<long long> ans;
    for (int i = 0; i < sz; ++i) {
        long long last = i ? ans.back() : 0;
        long long choose = maxN - last + 1;
        ans.push_back((long long)(rng()) % choose + last + 1LL);
    }
    return ans;
}

vector<pair<int, int>> edges(vector<long long> const& indices, int V) {
    vector<pair<int, int>> ans;
    V;
    long long cur = 0;
    int j = 0;
    for (int i = 0; i < (int)(indices.size()); ++i) {
        if (indices[i] < cur + V - j - 1) {
            ans.push_back({j, indices[i] - cur});
        } else {
            --i; ++j; cur += V - j;
        }
    }
    return ans;
}

Graph build_graph(int V, int E, mt19937_64& rng) {
    vector<long long> edge_indices = generate_random_subset(V * (V - 1) / 2, E, rng);
    vector<pair<int, int>> edge_list = edges(edge_indices, V);
    vector<int> perm = generate_random_permutation(V, rng);
    // TODO : Check paths that aren't at don't have at least length 3 and append them to the first or the last one
    Graph G(V);
    for (auto e : edge_list) G.add_edge(perm[e.first], perm[e.second]);
    G.elongatePaths();
}

Graph build_random_graph(int max_v, int max_e, mt19937_64& rng) {
    int V = 9 * max_v / 10 + (rng() % max_v / 10);
    int E = 8 * max_e / 10 + (rng() % max_e / 10); // this is so we can add some more if needed
    return build_graph(V, E, rng);
}


Graph build_random_graph_one_articulation(int max_v, int max_e, mt19937_64& rng) {
    int V1 = 4 * max_v / 10 + (rng() % max_v) / 10;

}