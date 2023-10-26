#include <iostream>

using namespace std;

typedef long long ll;

ll powmod(ll base, ll exponent, ll modulo) {
    ll ans = 1;
    for (ll i = 0; i < exponent; ++i) {
        ans = ans * base % modulo;
    }
    return ans;
}

/**
* Return the number of unique Jenga towers that can be built using N or fewer
* bricks. Give your answer modulo 3359232.
* 
* N: the maximum number of bricks to use
*/
int solve(ll N) {
    ll mod = 3359232;
    int ans = 0;
    for (ll i = 0; i < N / 3; ++i) {
        ans += powmod(2, i, mod);
        ans %= mod;
    }
    return ans;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        ll N;
        cin >> N;
        cout << solve(N) << '\n';
    }
}