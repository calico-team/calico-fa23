#include <iostream>
#include <vector>

using namespace std;

/**
 * Find the distance the subway must travel before all passengers
 * arrive at their ending station
 * 
 * N: the number of passengers
 * M: the number of stations
 * K: the capacity of the train
 * S: the list of starting stations for each passenger
 * E: the list of ending stations for each passenger
 * P: the list of line positions for each passenger at their station
 */
int solve(int N, int M, int K, vector<int> S, vector<int> E, vector<int> P) {
    // YOUR CODE HERE
    return -1;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, M, K;
        cin >> N >> M >> K;
        vector<int> S(N);
        for (int &item : S) {
            cin >> item;
        }
        vector<int> E(N);
        for (int &item : E) {
            cin >> item;
        }
        vector<int> P(N);
        for (int &item : P) {
            cin >> item;
        }
        solve(N, M, K, S, E, P);
    }
}