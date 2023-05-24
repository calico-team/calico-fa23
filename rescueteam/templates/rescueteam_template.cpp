#include <iostream>
#include <vector>

using namespace std;

/**
  * Given the layout of a mystery dungeon, find the largest
  * value of treasure you can collect before running out of belly.
  * 
  * F: the number of floors in the mystery dungeon
  * B: your belly capacity
  * N: the number of nodes on each floor the of the mystery dungeon
  * M: the number of edges on each floor of the mystery dungeon
  * S: the node where the spawn point is located
  * E: the node where the exit stairwell is located
  * X: the list of X_i for each undirected edge
  * Y: the list of Y_i for each undirected edge
  * U: the node where the treasure on floor i is located
  * V: the value of the treasure on floor i
  */
void solve (int F, int B, int N, int M, int S, int E, vector<int> X, vector<int> Y, vector<int> U, vector<int> V) {
    // YOUR CODE HERE
}

int main () {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        int F, B, N, M, S, E;
        cin >> F >> B;
        cin >> N >> M >> S >> E;
        vector<int> X(M);
        vector<int> Y(M);
        vector<int> U(F);
        vector<int> V(F);
        for (int j = 0; j < M; ++j) {
            cin >> X[j] >> Y[j];
        }
        for (int j = 0; j < F; ++j) {
            cin >> U[j] >> V[j];
        }
        solve(F, B, N, M, S, E, X, Y, U, V);
    }
}