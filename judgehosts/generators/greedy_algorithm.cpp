#include <bits/stdc++.h>
using namespace std;

#define sz(x) int(x.size())

const int inf = INT_MAX / 2;

vector<int> priorities;

struct comp {
    bool operator () (int const& i, int const& j) const {
        return priorities[i] < priorities[j] || priorities[i] == priorities[j] && i < j;
    }
};

int greedy(int N, int M, int S, vector<int> const& U, vector<int> const& V) {
    vector<vector<int>> g(N), gt(N);
    vector<bool> sources(N, true), sinks(N, true);
    priorities.assign(N, 0);
    for (int i = 0; i < M; ++i) {
        g[U[i]-1].push_back(V[i]-1);
        gt[V[i]-1].push_back(U[i]-1);
        sources[V[i]-1] = false;
        sinks[U[i]-1] = false;
    }
    for (int i = 0; i < N; ++i) {
        for (int j : g[i]) {
            if (sinks[j]) priorities[i] = inf;
            else priorities[i]++;
        }
    }
    bool possible = true;
    set<int, comp> heap;
    for (int i = 0; i < N; ++i) {
        if (sources[i]) {
            for (int u : g[i]) {
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

    cerr <<  "aqui"  << endl;

    int minCut = possible ? sz(heap) : inf, cur = sz(heap);
    while (heap.size()) {
        int nxt = *heap.begin();
        heap.erase(heap.begin());
        cur--;
        for (int s : g[nxt]) {
            if (sinks[s]) cur = inf;
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
        minCut = min(minCut, cur);
    }

    return minCut;

}