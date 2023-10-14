#include <iostream>
#include <vector>
#include <queue>

using namespace std; 

int F, N, M, B, S, E;
pair<int, int> treasure[1005]; // index, value
vector<int> adj[100005];
int dp[1005][1005]; // maximum amount after going F floors with B belly left

vector<int> bfs(int src) {
    vector<int> dist(N, 1e9 + 7);
    vector<int> vis(N, 0);
    queue<int> q;
    q.push(src);
    dist[src] = 0;
    while (!q.empty()) {
        int tp = q.front();
        q.pop();
        if (vis[tp])
            continue;
        vis[tp] = 1;
        for (int nx : adj[tp]) {
            if (vis[nx]) continue;
            dist[nx] = min(dist[nx], dist[tp] + 1);
            q.push(nx);
        }
    }
    return dist;
}

void solve() {
    cin >> F >> B;
    cin >> N >> M >> S >> E;
    --S; --E; // zero based indexing WINS
    for (int i = 0; i < N; i++)
        adj[i].clear();
    for (int i = 0; i < M; i++) {
        int u, v; cin >> u >> v; --u; --v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    for (int i = 0; i < F; i++) {
        cin >> treasure[i].first >> treasure[i].second;
        -- treasure[i].first;
    }
    vector<int> d_start = bfs(S);
    vector<int> d_end = bfs(E);
    // base case: dp[0][B] = 0
    for (int i = 0; i <= F; i++) for (int j = 0; j <= B; j++) {
        dp[i][j] = -1e9;
    }
    int ans = 0;
    dp[0][B] = 0;
    for (int i = 0; i < F; i++) {
        int t1 = d_start[treasure[i].first] + d_end[treasure[i].first];
        int t2 = d_start[E];
        for (int j = B - t1; j >= 0; j--) {
            if (dp[i][j + t1] == -1e9) continue;
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j + t1] + treasure[i].second);
            ans = max(ans, dp[i + 1][j]);
        }
        for (int j = B - t2; j >= 0; j--) {
            if (dp[i][j + t2] == -1e9) continue;
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j + t2]);
            ans = max(ans, dp[i + 1][j]);
        }
    }
    cout << ans << endl;
}

int main() {
    int T; cin >> T;
    while (T--)
        solve();
}
