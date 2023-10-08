#include <iostream>

using namespace std;

typedef long long ll;

// We need to use long long instead of int because 10^18 >= 2^31
ll solve(ll N, ll K) {
    if (K % 2 == 0) {
        return K / 2;
    }
    
    if (N % 2 == 0) {
        return N / 2 + solve(N / 2, K / 2 + 1);
    } else {
        if (K == 1) {
            return N / 2 + 1;
        }
        return N / 2 + 1 + solve(N / 2, K / 2);
    }
}

int main() {
    int T;
    ll N, K;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N >> K;
        cout << solve(N, K) << '\n';
    }
}
