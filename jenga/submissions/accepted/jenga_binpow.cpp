#include <iostream>

using namespace std;

typedef long long ll;

ll binpow(ll base, ll exponent, ll modulo) {
    ll ans = 1;
    while (exponent) {
        if (exponent & 1)
            ans = ans * base % modulo;
        base = base * base % modulo;
        exponent /= 2;
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
    return int((binpow(2, 1 + N / 3, mod) + mod - 2) % mod);
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