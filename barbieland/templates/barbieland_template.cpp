#include <iostream>
#include <vector>

using namespace std;

using ll = long long;

/**
 * Output Q lines, where the i-th line contains the maximum
 * route length possible for the i-th query
 *     
 * N: the number of dreamhouses
 * M: the number of roads
 * Q: the number of queries
 * U: the list of U_i for each road
 * V: the list of V_i for each road
 * W: the list of W_i for each road
 * A: the list of A_i for each query
 * B: the list of B_i for each query
 * 
 */
void solve(int N, int M, int Q, vector<int>& U, vector<int>& V, vector<ll>& W, vector<int>& A, vector<int>& B) {
    // YOUR CODE HERE
    return;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, M, Q;
        cin >> N >> M >> Q;
        vector<int> U(M), V(M), A(Q), B(Q);
        vector<ll> W(M);
        for (int j = 0; j < M; ++j) {
            cin >> U[j] >> V[j] >> W[j];
        }
        for (int j = 0; j < Q; ++j) {
            cin >> A[j] >> B[j];
        }
        solve(N, M, Q, U, V, W, A, B);
    }
}
