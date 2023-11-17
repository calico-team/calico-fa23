#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

/**
  * Given the layout of a mystery dungeon, find the largest
  * number of treasures you can collect before running out of belly.
  * F: the number of floors in the mystery dungeon
  * B: your belly value
  * N: the number of nodes on each floor the of the mystery dungeon
  * M: the number of edges on each floor of the mystery dungeon
  * S: the node where the starting room of each floor is located
  * E: the node where the exit room of each floor is located
  * R: the list of room indices where each treasure room is located
  * U: the list of Ui for each hallway
  * V: the list of Vi for each hallway
  */
int solve (int F, int B, int N, int M, int S, int E, vector<int>& R, vector<int>& U, vector<int>& V) {
    // YOUR CODE HERE
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
    // dp min belly to get at least E food eaten
    vector<int> dp(F+1, inf);
    dp[0] = 0;
    int ans = 0;
    for(int i = 0; i < F; i++){
        // Currently at floor i
        vector<int> new_dp(F+1, inf);
        for(int j = 0; j <= F; j++){
            // Try to get j treasure
            // If we want to add a treasure, add dist to treasure, then to exit
            // Go to K[i] and then go to the exit
            if(j-1 >= 0)
                new_dp[j] = min(new_dp[j], dp[j-1] + dist_to_start[R[i]] + dist_to_end[R[i]]);
            // Don't take a treasure on this floor
            new_dp[j] = min(new_dp[j], dp[j] + dist_to_end[S]);
        }
        for(int i = 0; i <= F; i++){
            if(dp[i] <= B){
                ans = max(ans, i);
            }
            if(new_dp[i] <= B){
                ans = max(ans, i);
            }
        }
        dp = new_dp;
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