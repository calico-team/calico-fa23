#include <iostream>
#include <vector>

using namespace std;

/**
 * Find the total distance the subway must travel until all passengers have
 * arrived at their ending station.
 * 
 * N: the number of passengers
 * M: the number of stations
 * K: the maximum number of passengers the subway can carry
 * S: list of starting stations for each passenger
 * E: list of ending stations for each passenger
 * P: list of positions in line at their starting station for each passenger
 */
int solve(int N, int M, int K, vector<int> &S, vector<int> &E, vector<int> &P) {
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
        cout << solve(N, M, K, S, E, P) << '\n';
    }
}
