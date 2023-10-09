#include <iostream>
#include <vector>
#include <queue>

using namespace std;

/**
 * Print in the first line the number K of computers Bessie the Cow should eat.
 * Print in the next line K numbers, one for each different computer she should eat.
 * If her task is not possible, print "IMPOSSIBLE"
 * 
 * @param N Number of computers.
 * @param M Number of connections between computers.
 * @param S Number of stomachs.
 * @param U Initial computer for each of the M connections.
 * @param V Final computer for each of the M connections.
 * 
*/
void solve(int N, int M, int S, vector<int>& U, vector<int>& V) {
    vector<vector<int>> adjList(N);
    vector<int> inDeg(N), outDeg(N);
    for (int i = 0; i < M; ++i) {
        adjList[--U[i]].push_back(--V[i]);
        ++inDeg[V[i]];
        ++outDeg[U[i]];
    }
    queue<int> bfs_queue;
    vector<bool> visited(N);
    for (int i = 0; i < N; ++i) if (!inDeg[i]) bfs_queue.push(i);
    while (!bfs_queue.empty()) {
        if (bfs_queue.size() <= S && visited[bfs_queue.front()] && !outDeg[bfs_queue.front()]) {
            int K = (int)(bfs_queue.size());
            for (int i = 0; i < K - 1; ++i) {
                cout << bfs_queue.front() << ' ';
                bfs_queue.pop();
            }
            cout << bfs_queue.front() << '\n';
            return;
        }
        int u = bfs_queue.front(); bfs_queue.pop();
        for (int v : adjList[u]) {
            if (!visited[v]) {
                visited[v] = true;
                bfs_queue.push(v);
            }
        }
    }
    cout << "IMPOSSIBLE\n";
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