#include <iostream>
#include <vector>
#include <climits>
using namespace std;

using ll = long long;

/**
 * Description: Calculates maximum flow of a graph
 * Time: $O(N^2M)$ flow, $O(M\sqrt N)$ bipartite matching
 * Source: KACTL, https://github.com/kth-competitive-programming/kactl/blob/main/content/graph/Dinic.h
 */

struct PushRelabel {
	struct Edge { int dest, back; ll f, c; };
	vector<vector<Edge>> g;
	vector<ll> ec;
	vector<Edge*> cur;
	vector<vector<int>> hs; vector<int> H;
	PushRelabel(int n) : g(n),ec(n),cur(n),hs(2*n),H(n){}

	void addEdge(int s, int t, ll cap, ll rcap=0) {
		if (s == t) return;
		g[s].push_back({t, int(g[t].size()), 0, cap});
		g[t].push_back({s, int(g[s].size())-1, 0, rcap});
	}

	void addFlow(Edge& e, ll f) {
		Edge &back = g[e.dest][e.back];
		if (!ec[e.dest] && f) hs[H[e.dest]].push_back(e.dest);
		e.f += f; e.c -= f; ec[e.dest] += f;
		back.f -= f; back.c += f; ec[back.dest] -= f;
	}
	ll calc(int s, int t) {
		int v = int(g.size()); H[s] = v; ec[t] = 1;
		vector<int> co(2*v); co[0] = v-1;
		for (int i = 0; i < v; ++i) cur[i] = g[i].data();
		for (Edge& e : g[s]) addFlow(e, e.c);
		for (int hi = 0;;) {
			while (hs[hi].empty()) if (!hi--) return -ec[s];
			int u = hs[hi].back(); hs[hi].pop_back();
			while (ec[u] > 0)
				if (cur[u] == g[u].data() + int(g[u].size())) {
					H[u] = 1e9;
					for (Edge& e : g[u]) if (e.c && H[u] > H[e.dest]+1)
						H[u] = H[e.dest]+1, cur[u] = &e;
					if (++co[H[u]], !--co[hi] && hi < v)
						for (int i = 0; i < v; ++i) if (hi < H[i] && H[i] < v)
							--co[H[i]], H[i] = v + 1;
					hi = H[u];
				} else if (cur[u]->c && H[u] == H[cur[u]->dest]+1)
					addFlow(*cur[u], min(ec[u], cur[u]->c));
				else ++cur[u];
		}
	}
	bool leftOfMinCut(int a) { return H[a] >= int(g.size()); }
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
    PushRelabel flow(2 * N + 2);
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