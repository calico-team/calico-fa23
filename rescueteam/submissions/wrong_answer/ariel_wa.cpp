#include <bits/stdc++.h>
using namespace std;

void solve() {
    int F, B, N, M, S, E;
    cin >> F >> B >> N >> M >> S >> E; 
    S--; E--; 
    vector<int> k(F);
    for (int i = 0; i < F; i++) {
        int keynode; 
        cin >> keynode; 
        k[i] = keynode-1; 
    }
    vector<vector<int>> c(N);
    for (int i = 0; i < M; i++) {
        int x, y;
        cin >> x >> y; 
        c[x-1].push_back(y-1); 
        c[y-1].push_back(x-1); 
    }
    vector<int> sdist(N, -1); 
    queue<pair<int, int>> q;
    q.push({S, 0});
    while (!q.empty()) {
        int node = q.front().first, steps = q.front().second; 
        q.pop(); 
        if (sdist[node] != -1) continue; 
        sdist[node] = steps; 
        for (int neighbor : c[node]) {
            if (sdist[neighbor] == -1) q.push({neighbor, steps+1});
        }
    }
    vector<int> edist(N, -1);
    q.push({E, 0});
    while (!q.empty()) {
        int node = q.front().first, steps = q.front().second; 
        q.pop(); 
        if (edist[node] != -1) continue; 
        edist[node] = steps; 
        for (int neighbor : c[node]) {
            if (edist[neighbor] == -1) q.push({neighbor, steps+1});
        }
    }
    int SEdist = sdist[E]; 
    int sumTreasureTravels = 0; 
    int ans = 0; 
    multiset<int> s; 
    for (int i = 0; i < F; i++) {
        int bellyLeft = B - (i+1) * SEdist; 
        int treasureCost = sdist[k[i]] + edist[k[i]] - SEdist; 
        while (!s.empty() && sumTreasureTravels + treasureCost > bellyLeft && -*s.begin() > treasureCost) {
                sumTreasureTravels += *s.begin();
                s.erase(s.begin()); 
        }
        if (sumTreasureTravels + treasureCost <= bellyLeft) {
            sumTreasureTravels += treasureCost; 
            s.insert(-treasureCost); 
        }
        ans = max(ans, (int) s.size());
    }
    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    while (T--) solve(); 
}