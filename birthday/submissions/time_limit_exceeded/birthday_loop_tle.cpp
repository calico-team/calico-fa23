#include <iostream>
using namespace std;
typedef long long ll;

ll solve(ll N) {
    ll numDays = 0;
    for (int i = 1; i <= N; i++){
        numDays += ll(i) * ll(i);
    }
    return numDays - N;
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