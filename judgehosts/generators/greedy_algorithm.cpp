#include <bits/stdc++.h>
using namespace std;

#define sz(x) int(x.size())

vector<int> priorities;

struct comp {
    bool operator () (int i, int j) {
        return priorities[i] < priorities[j] || priorities[i] == priorities[j] && i < j;
    }
};

int solve(int N, int M, int S, vector<int> const& U, vector<int> const& V) {
    vector<vector<int>> g(N), gt(N);
    vector<bool> sources(N, false), sinks(N, false);
    priorities.assign(N, 0);
    for (int i = 0; i < M; ++i) {
        g[U[i]].push_back(V[i]);
        gt[V[i]].push_back(U[i]);
        sources[V[i]] = false;
        sinks[U[i]] = false;
    }
    int inf = S + 1;
    for (int i = 0; i < N; ++i) {
        for (int j : g[i]) {
            if (sinks[j]) priorities[i] += inf;
            else priorities[i]++;
        }
    }
    bool possible = true;
    set<int, comp> heap;
    for (int i = 0; i < N; ++i) {
        if (sources[i]) {
            for (int u : g[s]) {
                if (sinks[u]) possible = false;
                heap.insert(u);
                for (int v : gt[u]) {
                    bool isInTheHeap = heap.count(v);
                    if (isInTheHeap) heap.erase(v);
                    priorities[v]--;
                    if (isInTheHeap) heap.insert(v);
                }
            }
        }
    }

    int minCut = sz(heap), cur = sz(heap);
    while (heap.size()) {
        int nxt = *heap.begin();
        heap.erase(heap.begin());
        cur--;
        for (int u : g[nxt]) {
            if (sinks[u]) cur = INT_MAX / 2;
            else cur++;
            for (int u : g[s]) {
                if (sinks[u]) possible = false;
                heap.insert(u);
                for (int v : gt[u]) {
                    bool isInTheHeap = heap.count(v);
                    if (isInTheHeap) heap.erase(v);
                    priorities[v]--;
                    if (isInTheHeap) heap.insert(v);
                }
            }
        }
    }


    if (!possible) cout << "IMPOSSIBLE\n";
    else {
        for (int cowmputer : heap) cout << cowmputer << ' ';
        cout << '\n';
    }

}

int main() {

    int N, S;
    vector<vector<int>> g, gt; // g is the graph, gt is the traspose graph
    set<int> sources, sinks;
    // Read everything idk
    vector<bool> visited(N);
    priorities.assign(N, 0); // How many nodes they add up if I take this node if that makes sense

    for (int i = 0; i < N; ++i) {
        for (int j : g[i]) {
            if (sinks.count(j)) priorities[i] += inf;
            else priorities[i]++;
        }
    }

    priority_queue<ii, vector<ii>, greater<ii>> pq;

    bool possible = true;

    set<int, comp> heap;

    for (int s : sources) {
        for (int u : g[s]) {
            if (sinks.count(u)) possible = false;
            heap.insert(u);
            for (int v : gt[u]) {
                bool isInTheHeap = heap.count(v);
                if (isInTheHeap) heap.erase(v);
                priorities[v]--;
                if (isInTheHeap) heap.insert(v);
            }
        }
    }

    while (heap.size() > S) {
        int nxt = *heap.begin();
        heap.erase(nxt);
        for (int u : g[nxt]) {
            if (sinks.count(u)) possible = false;
            heap.insert(u);
            for (int v : gt[u]) {
                bool isInTheHeap = heap.count(v);
                if (isInTheHeap) heap.erase(v);
                priorities[v]--;
                if (isInTheHeap) heap.insert(v);
            }
        }
    }

    if (!possible) cout << "IMPOSSIBLE\n";
    else {
        for (int cowmputer : heap) cout << cowmputer << ' ';
        cout << '\n';
    }

    return 0;

}