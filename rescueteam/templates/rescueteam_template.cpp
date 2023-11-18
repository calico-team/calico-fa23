#include <iostream>
#include <vector>

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