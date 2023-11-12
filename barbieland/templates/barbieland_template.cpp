#include <iostream>
#include <vector>

using namespace std;

using ll = long long;

/**
 * Output Q lines, where the i-th line contains the maximum
 * fuel charge possible for the i-th errand
 *     
 * N: the number of universes
 * M: the number of portals
 * Q: the number of queries
 * U: the list containing U_i for each query
 * V: the list containing V_i for each query
 * A: the list of A_i for each portal
 * B: the list of B_i for each portal
 * C: the list of fuel charges for each portal
 * 
 */
void solve(int N, int M, int Q, vector<int>& U, vector<int>& V, vector<int>& A, vector<int>& B, vector<ll>& C) {
    // YOUR CODE HERE
    return;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, M, Q;
        cin >> N >> M >> Q;
        vector<int> A(M);
        vector<int> B(M);
        vector<ll> C(M);
        for (int j = 0; j < M; j++) {
            cin >> A[j] >> B[j] >> C[j];
        }
        vector<int> U(Q), V(Q);
        for (int j = 0; j < Q; ++j) {
            cin >> U[j] >> V[j];
        }
        solve(N, M, Q, U, V, A, B, C);
    }
}
