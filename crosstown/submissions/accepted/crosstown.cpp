#include <iostream>
#include <vector>

using namespace std;

int solve(int N, int M, vector<int> &S, vector<int> &E) {
    int longest = 0;
    for (int i = 0; i < N; i++) {
        longest = max(longest, (E[i] - S[i] + M) % M);
    }
    return longest;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, M;
        cin >> N >> M;
        vector<int> S(N);
        for (int &item : S) {
            cin >> item;
        }
        vector<int> E(N);
        for (int &item : E) {
            cin >> item;
        }
        cout << solve(N, M, S, E) << '\n';
    }
}
