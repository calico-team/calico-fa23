#include <iostream>
using namespace std;
typedef long long ll;

ll solve(ll N) {
    return (N * (N + 1) * (2 * N + 1) / 6) - N;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        ll N;
        cin >> N;
        cout << solve(N) << '\n';
    }
    return 0;
}
