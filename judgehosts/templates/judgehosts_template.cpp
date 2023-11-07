#include <iostream>
#include <vector>

using namespace std;

/**
 * Output any list of x <= S computers Bessie can eat such that the network is not bridged afterwards.
 * If it's impossible, output IMPOSSIBLE
 * 
 * N: Number of computers.
 * M: Number of connections between computers.
 * S: Number of computers Bessie can eat.
 * U: Initial computer for each of the M connections.
 * V: Final computer for each of the M connections.
 * 
*/
void solve(int N, int M, int S, vector<int>& U, vector<int>& V) {
    // YOUR CODE HERE
    return;
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