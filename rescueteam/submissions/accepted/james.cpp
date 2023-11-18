#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

int solve (int F, int B, int N, int M, int S, int E, vector<int>& R, vector<int>& U, vector<int>& V) {
    int inf = 2e9;
    vector<vector<int>> adj(N+1);
    for(int i = 0; i < M; i++){
        adj[U[i]].push_back(V[i]);
        adj[V[i]].push_back(U[i]);
    }
    auto bfs = [&](vector<int> &dist, int source){
        for(int i = 0; i <= N; i++){
            dist[i] = inf;
        }
        dist[source] = 0;
        queue<int> q;
        q.push(source);
        while(q.size()){
            int u = q.front();
            q.pop();
            for(int c: adj[u]){
                if(dist[c] == inf){
                    dist[c] = dist[u] + 1;
                    q.push(c);
                }
            }
        }
    };
    vector<int> dist_to_start(N+1), dist_to_end(N+1);
    bfs(dist_to_start, S);
    bfs(dist_to_end, E);
    priority_queue<int> pq;
    int cnt = 0, ans = 0;
    int belly = 0;
    for(int i = 0; i < F; i++){
        int direct = dist_to_end[S];
        int treasure = dist_to_start[R[i]] + dist_to_end[R[i]];
        cnt++;
        belly += treasure;  // Assume that we took treasure at this floor
        // We can undo our decision here by instead going directly to next floor
        pq.push(treasure - direct);
        while(pq.size() && belly > B){
            belly -= pq.top();
            pq.pop();
            cnt--;
        }
        // belly
        if(cnt == 0 && belly + direct > B){
            break;
        }
        if(belly <= B)
            ans = max(ans, cnt);
    }
    return ans;
}

int main () {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        int F, B, N, M, S, E;
        cin >> F >> B;
        cin >> N >> M >> S >> E;
        vector<int> R(F);
        for (int j = 0; j < F; ++j) {
            cin >> R[j];
        }
        vector<int> U(M), V(M);
        for (int j = 0; j < M; ++j) {
            cin >> U[j] >> V[j];
        }
        cout << solve(F, B, N, M, S, E, R, U, V) << '\n';
    }
}
