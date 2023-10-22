#include <bits/stdc++.h>
using namespace std;

const int MOD = 3359232;

using ll = long long;
using vll = vector<ll>;
using vvll = vector<vll>;
#define pb push_back
#define sz(x) (int)(x.size())

/**
 * Description: Big Integer
 * Source: https://github.com/bqi343/cp-notebook/blob/master/Implementations/content/numerical/Arithmetic/BigInt.h
 */

// base and base_digits must be consistent
const int base = 1e9, base_digits = 9;
struct bigint { // value == 0 is represented by empty z
	vector<int> z; // digits
	int sign; // sign == 1 <==> value >= 0
	bigint() : sign(1) {} // sign == -1 <==> value < 0
	bigint(ll v) { *this = v; }
	bigint &operator=(ll v) {
		sign = v < 0 ? -1 : 1; v *= sign; // make v positive
		z.clear(); for (;v;v/=base) z.pb(v%base);
		return *this;
	}
	bigint(const string &s) { read(s); } // add char by char

	bigint &operator+=(const bigint &other) {
		//dbg("ADDING",*this,other,sign,other.sign);
		if (sign == other.sign) {
			for (int i = 0, carry = 0; i < sz(other.z) || carry; ++i) {
				if (i == sz(z)) z.pb(0);
				z[i] += carry+(i<sz(other.z)?other.z[i]:0);
				carry = z[i] >= base; if (carry) z[i] -= base;
			}
		} else if (other != 0 /* prevent infinite loop */) *this -= -other;
		return *this;
	}
	friend bigint operator+(bigint a, const bigint &b) { return a += b; }
	bigint &operator-=(const bigint &other) {
		if (sign == other.sign) {
			if ((sign == 1 && *this >= other) || (sign == -1 && *this <= other)) {
				for (int i = 0, carry = 0; i < sz(other.z) || carry; ++i) {
					z[i] -= carry+(i<sz(other.z)?other.z[i]:0);
					carry = z[i]<0; if (carry) z[i] += base;
				}
				trim();
			} else { // result will change sign
				*this = other-*this;
				this->sign = -this->sign;
			}
		} else *this += -other;
		return *this;
	}
	friend bigint operator-(bigint a, const bigint &b) { return a -= b; }

	bigint &operator*=(int v) { // oops make sure not to multiply by ll ...
		if (v < 0) sign = -sign, v = -v;
		for (int i = 0, carry = 0; i < sz(z) || carry; ++i) {
			if (i == sz(z)) z.pb(0);
			ll cur = (ll)z[i]*v+carry;
			carry = cur/base; z[i] = cur%base;
		}
		trim(); return *this;
	}
	bigint operator*(int v) const { return bigint(*this) *= v; }
	friend pair<bigint, bigint> divmod(const bigint &a1, const bigint &b1) {
		int norm = base/(b1.z.back()+1);
		bigint a = a1.abs()*norm, b = b1.abs()*norm, q, r; // make last element of b big
		q.z.resize(sz(a.z));
		for (int i = sz(a.z) - 1; i >= 0; --i) {
			r *= base; r += a.z[i];
			int s1 = sz(b.z) < sz(r.z) ? r.z[sz(b.z)] : 0;
			int s2 = sz(b.z)-1 < sz(r.z) ? r.z[sz(b.z)-1] : 0;
			int d = ((ll)s1*base+s2)/b.z.back(); // best approximation
			r -= b*d; while (r < 0) r += b, --d;
			q.z[i] = d;
		}
		q.sign = a1.sign*b1.sign; r.sign = a1.sign;
		q.trim(); r.trim(); return {q,r/norm};
	}
	bigint operator/(const bigint &v) const { return divmod(*this, v).first; }
	bigint operator%(const bigint &v) const { return divmod(*this, v).second; }
	bigint &operator/=(int v) {
		if (v < 0) sign = -sign, v = -v;
		for (int i = sz(z)-1, rem = 0; i >= 0; --i) {
			ll cur = z[i]+rem*(ll)base;
			z[i] = cur/v; rem = cur%v;
		}
		trim(); return *this;
	}
	bigint operator/(int v) const { return bigint(*this) /= v; }
	int operator%(int v) const {
		if (v < 0) v = -v;
		int m = 0; for (int i = sz(z) - 1; i >= 0; --i) m = (z[i]+m*(ll)base)%v;
		return m*sign; }
	bigint &operator*=(const bigint &v) { return *this = *this*v; }
	bigint &operator/=(const bigint &v) { return *this = *this/v; }

	bool operator<(const bigint &v) const {
		if (sign != v.sign) return sign < v.sign;
		if (sz(z) != sz(v.z)) return sz(z)*sign < sz(v.z) * v.sign;
		for (int i = sz(z) - 1; i >= 0; --i) if (z[i] != v.z[i]) return z[i]*sign < v.z[i]*sign;
		return 0; // equal
	}
	bool operator>(const bigint &v) const { return v < *this; }
	bool operator<=(const bigint &v) const { return !(v < *this); }
	bool operator>=(const bigint &v) const { return !(*this < v); }
	bool operator==(const bigint &v) const { return !(*this < v) && !(v < *this); }
	bool operator!=(const bigint &v) const { return *this < v || v < *this; }
	void trim() {
		while (sz(z) && z.back() == 0) z.pop_back();
		if (!sz(z)) sign = 1; // don't output -0
	}
	bool isZero() const { return !sz(z); }
	friend bigint operator-(bigint v) {
		if (sz(v.z)) v.sign = -v.sign;
		return v; }
	bigint abs() const { return sign == 1 ? *this : -*this; }
	ll longValue() const {
		ll res = 0; for (int i = sz(z) - 1; i >= 0; --i) res = res*base+z[i];
		return res*sign; }

	void read(const string &s) {
		sign = 1; z.clear(); int pos = 0;
		while (pos < sz(s) && (s[pos] == '-' || s[pos] == '+')) {
			if (s[pos] == '-') sign = -sign;
			++pos; } // account for sign
		for (int i = sz(s)-1; i >= pos; i -= base_digits) {
			int x = 0;
			for (int j = max(pos, i-base_digits+1); j <= i; j++)
				x = x*10+s[j]-'0';
			z.pb(x);
		}
		trim();
	}
	bigint operator*(const bigint &v) const {
		return mul_simple(v);
	}
	bigint mul_simple(const bigint &v) const {
		bigint res; res.sign = sign*v.sign;
		res.z.resize(sz(z)+sz(v.z));
		for (int i = 0; i < sz(z); ++i) if (z[i]) {
			ll cur = 0; for (int j = 0; j < sz(v.z) || cur; ++j) {
				cur += res.z[i+j]+(ll)z[i]*(j<sz(v.z)?v.z[j]:0);
				res.z[i+j] = cur%base; cur /= base;
			}
		}
		res.trim(); return res;
	}
};


vvll matMul(vvll const& A, vvll const& B) {
	int x = sz(A), y = sz(A[0]), z = sz(B[0]);
	assert(y == sz(B));
	vvll C(x, vll(z));
	for (int i = 0; i < x; ++i)
		for (int j = 0; j < y; ++j)
			for (int k = 0; k < z; ++k) {
				C[i][k] += A[i][j] * B[j][k];
				if (C[i][k] >= MOD) C[i][k] %= MOD;
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
int solve(string const& N) {
    // YOUR CODE HERE
	bigint pwr = N;
	pwr = (pwr / 3) % LAMBDA;
	return (int)((matPow(A, pwr.longValue())[dim_A - 1][0] - 1) + MOD) % MOD;
    
}

int main() {
    int T;
    cin >> T;
	vvll B = A;	
    for (int i = 0; i < T; i++) {
        string N;
        cin >> N;
        cout << solve(N) << '\n';
    }
	
}