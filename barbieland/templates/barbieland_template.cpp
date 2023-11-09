#include <iostream>
#include <vector>

using namespace std;

/**
 * Output a single line containing K - 1 space-separated values denoting
 * the maximum fuel charge possible for each leg of the journey.
 *     
 * N: the number of universes
 * M: the number of portals
 * K: the number of errands
 * U: the list containing the sequence of universes in which errands are to be completed
 * A: the list of A_i for each portal
 * B: the list of B_i for each portal
 * C: the list of fuel charges for each portal
 */
void solve(int N, int M, int K, vector<int> U, vector<int> A, vector<int> B, vector<int> C) {
    // YOUR CODE HERE
    return;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, M, K;
        cin >> N >> M >> K;
        vector<int> U(K);
        for (int &universe: U) {
            cin >> universe;
        }
        vector<int> A(M);
        vector<int> B(M);
        vector<int> C(M);
        for (int j = 0; j < M; j++) {
            cin >> A[j] >> B[j] >> C[j];
        }
        solve(N, M, K, U, A, B, C);
    }
}
