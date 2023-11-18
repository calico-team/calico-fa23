#include <bits/stdc++.h>
using namespace std;

const int MOD = 3359232;

using ll = long long;
using vll = vector<ll>;
using vvll = vector<vll>;
#define pb push_back
#define sz(x) (int)(x.size())

vvll matMul(vvll const& A, vvll const& B) {
	int x = sz(A), y = sz(A[0]), z = sz(B[0]);
	assert(y == sz(B));
	vvll C(x, vll(z));
	for (int i = 0; i < x; ++i)
		for (int j = 0; j < y; ++j)
			for (int k = 0; k < z; ++k) {
				C[i][k] += A[i][j] * B[j][k];
				C[i][k] %= MOD;
			}
	return C;
}

vvll matPow(vvll A, ll P) {
	vvll B(sz(A), vll(sz(A)));
	for (int i = 0; i < sz(A); ++i) B[i][i] = 1;
	for (;P;P/=2,A=matMul(A,A)) if (P & 1) B = matMul(B, A);
	return B;
}

vvll A =
{
	{ 2, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0 },
	{ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
	{ 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 },
	{ 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0 },
	{ 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0 },
	{ 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0 },
	{ 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
	{ 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
	{ 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0 },
	{ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
	{ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0 },
	{ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
	{ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 },
	{ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0 },
	{ 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0 },
	{ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
	{ 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0 },
	{ 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0 },
	{ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 }
};

const int dim_A = 19;

ll LAMBDA = (ll) 84LL * 312LL * 6LL * (ll) MOD;

/**
* Return the number of unique Benga towers that can be built using N or fewer
* bricks. Give your answer modulo 3359232.
* 
* N: the maximum number of bricks to use
*/
int solve(ll N) {
	return (int)(matPow(A, N / 3 + 1)[dim_A - 1][0] + MOD - 1) % MOD;
}

int main() {
    int T;
    cin >> T;
	vvll B = A;	
    for (int i = 0; i < T; i++) {
        ll N;
        cin >> N;
        cout << solve(N) << '\n';
    }
	
}