#include <iostream>
#include <vector>

using namespace std;

/**
 * 
 * @param N Number of computers.
 * @param M Number of connections between computers.
 * @param S Number of stomachs.
 * @param U Initial computer for each of the M connections.
 * @param V Final computer for each of the M connections.
 * 
 * @return  True if Bessie the Cow can eat enough computers with
 *          her S stomachs so that no submission is judged. False otherwise.
 * 
*/
void solve(int N, int M, int S, vector<int>& U, vector<int>& V) {
    // YOUR CODE HERE
    // Print in the first line the number of computers Bessie the Cow should eat
    // Print in the next line each of the computers she should eat
    // If it's impossible for Bessie the Cow to ruin the contest, print "IMPOSSIBLE"
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
}