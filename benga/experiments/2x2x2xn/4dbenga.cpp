/**
 * TEMPLATE
 * Source: (BenQ) https://github.com/bqi343/cp-notebook/blob/master/Implementations/content/contest/TemplateShort.cpp
*/

#include <bits/stdc++.h>
using namespace std;
 
using ll = long long;
using db = long double; // or double if tight TL
using str = string;

using pi = pair<int,int>;
#define mp make_pair
#define f first
#define s second

#define tcT template<class T
tcT> using V = vector<T>; 
tcT, size_t SZ> using AR = array<T,SZ>;
using vi = V<int>;
using vb = V<bool>;
using vpi = V<pi>;
using vl = V<ll>;
using pl = pair<ll, ll>;

#define sz(x) int((x).size())
#define all(x) begin(x), end(x)
#define sor(x) sort(all(x))
#define rsz resize
#define pb push_back
#define ft front()
#define bk back()

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define F0R(i,a) FOR(i,0,a)
#define ROF(i,a,b) for (int i = (b)-1; i >= (a); --i)
#define R0F(i,a) ROF(i,0,a)
#define rep(a) F0R(_,a)
#define each(a,x) for (auto& a: x)

const db PI = acos((db)-1);
mt19937 rng(0); // or mt19937_64

tcT> bool ckmin(T& a, const T& b) {
	return b < a ? a = b, 1 : 0; } // set a = min(a,b)
tcT> bool ckmax(T& a, const T& b) {
	return a < b ? a = b, 1 : 0; } // set a = max(a,b)





/**
 * Description: modular arithmetic operations 
 * Source: (BenQ) https://github.com/bqi343/cp-notebook/blob/master/Implementations/content/number-theory%20(11.1)/Modular%20Arithmetic/ModInt.h
 */


const int MOD = 1000000000;


template<int MOD, int RT> struct mint {
	static const int mod = MOD;
	static constexpr mint rt() { return RT; } // primitive root for FFT
	int v; explicit operator int() const { return v; } // explicit -> don't silently convert to int
	mint():v(0) {}
	mint(ll _v) { v = int((-MOD < _v && _v < MOD) ? _v : _v % MOD);
		if (v < 0) v += MOD; }
	bool operator==(const mint& o) const {
		return v == o.v; }
	friend bool operator!=(const mint& a, const mint& b) { 
		return !(a == b); }
	friend bool operator<(const mint& a, const mint& b) { 
		return a.v < b.v; }
	// friend void re(mint& a) { ll x; re(x); a = mint(x); }
	// friend str ts(mint a) { return ts(a.v); }
   
	mint& operator+=(const mint& o) { 
		if ((v += o.v) >= MOD) v -= MOD; 
		return *this; }
	mint& operator-=(const mint& o) { 
		if ((v -= o.v) < 0) v += MOD; 
		return *this; }
	mint& operator*=(const mint& o) { 
		v = int((ll)v*o.v%MOD); return *this; }
	mint& operator/=(const mint& o) { return (*this) *= inv(o); }
	friend mint pow(mint a, ll p) {
		mint ans = 1; assert(p >= 0);
		for (; p; p /= 2, a *= a) if (p&1) ans *= a;
		return ans; }
	friend mint inv(const mint& a) { assert(a.v != 0); 
		return pow(a,MOD-2); }
		
	mint operator-() const { return mint(-v); }
	mint& operator++() { return *this += 1; }
	mint& operator--() { return *this -= 1; }
	friend mint operator+(mint a, const mint& b) { return a += b; }
	friend mint operator-(mint a, const mint& b) { return a -= b; }
	friend mint operator*(mint a, const mint& b) { return a *= b; }
	friend mint operator/(mint a, const mint& b) { return a /= b; }
};

using mi = mint<MOD,5>; // 5 is primitive root for both common mods
using vmi = V<mi>;
using pmi = pair<mi,mi>;
using vpmi = V<pmi>;

inline ostream& operator << (ostream& o, mi const& m) { return o << int(m); }


/**
 * Description: 2D matrix operations.
 * Source: (BenQ) https://github.com/bqi343/cp-notebook/blob/master/Implementations/content/numerical/Matrix%20(11.3)/Matrix.h
 */

using T = mi;
using Mat = V<V<T>>; // use array instead if tight TL

Mat makeMat(int r, int c) { return Mat(r,V<T>(c)); }
Mat makeId(int n) { 
	Mat m = makeMat(n,n); F0R(i,n) m[i][i] = 1;
	return m;
}
Mat& operator+=(Mat& a, const Mat& b) {
	assert(sz(a) == sz(b) && sz(a[0]) == sz(b[0]));
	F0R(i,sz(a)) F0R(j,sz(a[0])) a[i][j] += b[i][j];
	return a;
}
Mat& operator-=(Mat& a, const Mat& b) {
	assert(sz(a) == sz(b) && sz(a[0]) == sz(b[0]));
	F0R(i,sz(a)) F0R(j,sz(a[0])) a[i][j] -= b[i][j];
	return a;
}
Mat operator+(Mat a, const Mat& b) { return a += b; }
Mat operator-(Mat a, const Mat& b) { return a -= b; }
V<T> operator*(const Mat& l, const V<T>& r) {
	assert(sz(l[0]) == sz(r));
	V<T> ret(sz(l));
	F0R(i,sz(l)) F0R(j,sz(l[0])) ret[i] += l[i][j]*r[j];
	return ret;
}
Mat operator*(const Mat& a, const Mat& b) {
	int x = sz(a), y = sz(a[0]), z = sz(b[0]); 
	assert(y == sz(b)); Mat c = makeMat(x,z);
	F0R(i,x) F0R(j,y) F0R(k,z) c[i][k] += a[i][j]*b[j][k];
	return c;
}
Mat& operator*=(Mat& a, const Mat& b) { return a = a*b; }
Mat pow(Mat m, ll p) {
	int n = sz(m); assert(n == sz(m[0]) && p >= 0);
	Mat res = makeId(n);
	for (; p; p /= 2, m *= m) if (p&1) res *= m;
	return res;
}






/**
 * Description: Big Integer
 * Source: (BenQ) https://github.com/bqi343/cp-notebook/blob/master/Implementations/content/numerical/Arithmetic/BigInt.h
 */

// base and base_digits must be consistent
const int base = 1e9, base_digits = 9;
struct bigint { // value == 0 is represented by empty z
	vi z; // digits
	int sign; // sign == 1 <==> value >= 0
	bigint() : sign(1) {} // sign == -1 <==> value < 0
	bigint(ll v) { *this = v; }
	bigint &operator=(ll v) {
		sign = v < 0 ? -1 : 1; v *= sign; // make v positive
		z.clear(); for (;v;v/=base) z.pb(v%base);
		return *this;
	}
	bigint(const str &s) { read(s); } // add char by char

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
		int norm = base/(b1.z.bk+1);
		bigint a = a1.abs()*norm, b = b1.abs()*norm, q, r; // make last element of b big
		q.z.rsz(sz(a.z));
		R0F(i,sz(a.z)) {
			r *= base; r += a.z[i];
			int s1 = sz(b.z) < sz(r.z) ? r.z[sz(b.z)] : 0;
			int s2 = sz(b.z)-1 < sz(r.z) ? r.z[sz(b.z)-1] : 0;
			int d = ((ll)s1*base+s2)/b.z.bk; // best approximation
			r -= b*d; while (r < 0) r += b, --d;
			q.z[i] = d;
		}
		q.sign = a1.sign*b1.sign; r.sign = a1.sign;
		q.trim(); r.trim(); return {q,r/norm};
	}
	friend bigint sqrt(const bigint &a1) {
		bigint a = a1; while (!sz(a.z) || sz(a.z)&1) a.z.pb(0);
		int n = sz(a.z), firstDigit = ::sqrt((db)a.z[n-1]*base+a.z[n-2]);
		int norm = base/(firstDigit+1); a *= norm; a *= norm;
		while (!sz(a.z) || sz(a.z)&1) a.z.pb(0);
		bigint r = (ll)a.z[n-1]*base+a.z[n-2];
		firstDigit = (int)::sqrt((db)a.z[n-1]*base+a.z[n-2]);
		int q = firstDigit; bigint res;
		R0F(j,n/2) {
			for (;; --q) {
				bigint r1 = (r-(res*2*base+q)*q)*base*base +
							(j>0?(ll)a.z[2*j-1]*base+a.z[2*j-2]:0);
				if (r1 >= 0) { r = r1; break; }
			}
			res *= base; res += q; // add a bit to sqrt
			if (j > 0) {
				int d1 = sz(res.z)+2 < sz(r.z) ? r.z[sz(res.z)+2] : 0; // always 0/1?
				int d2 = sz(res.z)+1 < sz(r.z) ? r.z[sz(res.z)+1] : 0;
				int d3 = sz(res.z) < sz(r.z) ? r.z[sz(res.z)] : 0;
				q = ((ll) d1*base*base+(ll)d2*base+d3)/(firstDigit*2);
			}
		}
		res.trim(); return res/norm;
	}
	bigint operator/(const bigint &v) const { return divmod(*this, v).f; }
	bigint operator%(const bigint &v) const { return divmod(*this, v).s; }
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
		int m = 0; R0F(i,sz(z)) m = (z[i]+m*(ll)base)%v;
		return m*sign; }
	bigint &operator*=(const bigint &v) { return *this = *this*v; }
	bigint &operator/=(const bigint &v) { return *this = *this/v; }

	bool operator<(const bigint &v) const {
		if (sign != v.sign) return sign < v.sign;
		if (sz(z) != sz(v.z)) return sz(z)*sign < sz(v.z) * v.sign;
		R0F(i,sz(z)) if (z[i] != v.z[i]) return z[i]*sign < v.z[i]*sign;
		return 0; // equal
	}
	bool operator>(const bigint &v) const { return v < *this; }
	bool operator<=(const bigint &v) const { return !(v < *this); }
	bool operator>=(const bigint &v) const { return !(*this < v); }
	bool operator==(const bigint &v) const { return !(*this < v) && !(v < *this); }
	bool operator!=(const bigint &v) const { return *this < v || v < *this; }
	void trim() {
		while (sz(z) && z.bk == 0) z.pop_back();
		if (!sz(z)) sign = 1; // don't output -0
	}
	bool isZero() const { return !sz(z); }
	friend bigint operator-(bigint v) {
		if (sz(v.z)) v.sign = -v.sign;
		return v; }
	bigint abs() const { return sign == 1 ? *this : -*this; }
	ll longValue() const {
		ll res = 0; R0F(i,sz(z)) res = res*base+z[i];
		return res*sign; }
	friend bigint gcd(const bigint &a, const bigint &b) {
		return b.isZero() ? a : gcd(b, a % b); } // euclidean algo
	friend bigint lcm(const bigint &a, const bigint &b) {
		return a/gcd(a, b) * b; }

	void read(const str &s) {
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
	friend istream &operator>>(istream &is, bigint &v) {
		str s; is >> s; v.read(s); return is; }
	friend ostream &operator<<(ostream &os, const bigint &v) {
		if (v.sign == -1) os << '-';
		os << (!sz(v.z) ? 0 : v.z.bk);
		R0F(i,sz(v.z)-1) os << setw(base_digits) << setfill('0') << v.z[i];
		return os; // pad with zeroes
	}
	static vi convert_base(const vi &a, int old_digits, int new_digits) {
		vl p(max(old_digits, new_digits) + 1); // blocks of 10^{old} -> 10^{new}
		p[0] = 1; FOR(i,1,sz(p)) p[i] = p[i-1]*10;
		vi res; ll cur = 0; int cur_digits = 0;
		for (int v:a) {
			cur += v*p[cur_digits]; cur_digits += old_digits;
			while (cur_digits >= new_digits) {
				res.pb(cur%p[new_digits]);
				cur /= p[new_digits]; cur_digits -= new_digits;
			}
		}
		res.pb(cur); while (sz(res) && res.bk == 0) res.pop_back();
		return res;
	}
	static vl karatMul(const vl &a, const vl &b) { // karatsuba
		int n = sz(a); vl res(2*n);
		if (n <= 32) { // naive multiply
			F0R(i,n) F0R(j,n) res[i+j] += a[i]*b[j];
			return res; }
		int k = n/2;
		vl a1(begin(a),begin(a)+k), a2(k+all(a));
		vl b1(begin(b),begin(b)+k), b2(k+all(b));
		vl a1b1 = karatMul(a1, b1), a2b2 = karatMul(a2, b2);
		F0R(i,k) a2[i] += a1[i], b2[i] += b1[i];
		vl r = karatMul(a2, b2); // three instead of four products
		F0R(i,sz(a1b1)) r[i] -= a1b1[i];
		F0R(i,sz(a2b2)) r[i] -= a2b2[i];
		F0R(i,sz(r)) res[i+k] += r[i];
		F0R(i,sz(a1b1)) res[i] += a1b1[i];
		F0R(i,sz(a2b2)) res[i+n] += a2b2[i];
		return res;
	}
	bigint operator*(const bigint &v) const {
		if (min(sz(z),sz(v.z)) < 150) return mul_simple(v);
		bigint res; res.sign = sign*v.sign; // should work as long as # of digits isn't too large (> LLONG_MAX/10^{12})
		vi a6 = convert_base(this->z, base_digits, 6); // blocks of 10^6 instead of 10^9
		vi b6 = convert_base(v.z, base_digits, 6);
		vl a(all(a6)), b(all(b6));
		while (sz(a) < sz(b)) a.pb(0);
		while (sz(b) < sz(a)) b.pb(0);
		while (sz(a)&(sz(a)-1)) a.pb(0), b.pb(0); // make size power of 2
		vl c = karatMul(a, b);
		ll cur = 0; F0R(i,sz(c)) { // process carries
			cur += c[i]; res.z.pb(cur%1000000); cur /= 1000000; } 
		res.z = convert_base(res.z,6,base_digits); 
		res.trim(); return res;
	}
	bigint mul_simple(const bigint &v) const {
		bigint res; res.sign = sign*v.sign;
		res.z.rsz(sz(z)+sz(v.z));
		F0R(i,sz(z)) if (z[i]) {
			ll cur = 0; for (int j = 0; j < sz(v.z) || cur; ++j) {
				cur += res.z[i+j]+(ll)z[i]*(j<sz(v.z)?v.z[j]:0);
				res.z[i+j] = cur%base; cur /= base;
			}
		}
		res.trim(); return res;
	}
	friend str ts(const bigint& v) {
		stringstream ss; ss << v;
		str s; ss >> s; return s; }
};


// Actual 4D Benga

const int W = 2; // Width
const bool COMPRESSED = true;

using Cube = V<V<vi>>;

map<Cube, Cube> canon;

V<Cube> rotate(Cube& grid) {
    // @todo: vector of rotations
    V<Cube> rotations;
    Cube aux = grid;
    F0R(_, 4) {
        F0R(i, W) F0R(j, W) F0R(k, W) {
            aux[i][j][k] = grid[i][k][W - j - 1];
        }
        grid = aux;
        rotations.pb(aux);
    }
    F0R(_, 4) {
        F0R(i, W) F0R(j, W) F0R(k, W) {
            aux[i][j][k] = grid[j][W - i - 1][k];
        }
        grid = aux;
        rotations.pb(aux);
    }
    F0R(_, 4) {
        F0R(i, W) F0R(j, W) F0R(k, W) {
            aux[i][j][k] = grid[W - k - 1][j][i];
        }
        grid = aux;
        rotations.pb(aux);
    }
    return rotations;
}

Cube canonical(Cube& grid) { // lowest in lexicographical order amongst all rotations
    if (!COMPRESSED) return grid;
    if (canon.count(grid)) return canon[grid];
    Cube ans = grid;
    V<Cube> rotations = rotate(grid);
    each(r, rotations) { ans = min(ans, r); }
    each(r, rotations) canon[r] = ans;
    return ans;
}

map<Cube, int> idx;
int cnt = 0;

map<Cube, mi> funZ(Cube& grid, bool visible) {
    map<Cube, mi> ans;
    V<vb> ok(W, vb(W, true));
    F0R(i, W) F0R(j, W) F0R(k, W) if (grid[i][j][k]) ok[i][j] = false;
    F0R(bs, 1 << (W * W)) {
        bool okay = true;
        Cube nxt_grid = grid;
        F0R(i, W) F0R(j, W) {
            if ((bs & (1 << (i * W + j))) && !ok[i][j]) okay = false;
            else if (bs & (1 << (i * W + j))) {
                F0R(k, W) nxt_grid[i][j][k] = 1;
            }
        }
        if (visible) {
            FOR(i, 1, W - 1) FOR(j, 1, W - 1) FOR(k, 1, W - 1) if (!nxt_grid[i][j][k]) okay = false;
        }
        if (!okay) continue;
        ans[canonical(nxt_grid)] += 1;
    }
    return ans;
}

map<Cube, mi> funY(Cube& grid, bool visible) {
    map<Cube, mi> ans;
    V<vb> ok(W, vb(W, true));
    F0R(i, W) F0R(j, W) F0R(k, W) if (grid[i][j][k]) ok[i][k] = false;
    F0R(bs, 1 << (W * W)) {
        bool okay = true;
        Cube nxt_grid = grid;
        F0R(i, W) F0R(k, W) {
            if ((bs & (1 << (i * W + k))) && !ok[i][k]) okay = false;
            else if (bs & (1 << (i * W + k))) {
                F0R(j, W) nxt_grid[i][j][k] = 1;
            }
        }
        if (!okay) continue;
        each(edge, funZ(nxt_grid, visible)) ans[edge.f] += edge.s;
    }
    return ans;
}

map<Cube, mi> funX(Cube& grid, bool visible) {
    map<Cube, mi> ans;
    V<vb> ok(W, vb(W, true));
    F0R(i, W) F0R(j, W) F0R(k, W) if (grid[i][j][k]) ok[j][k] = false;
    F0R(bs, 1 << (W * W)) {
        bool okay = true;
        Cube nxt_grid = grid;
        F0R(j, W) F0R(k, W) {
            if ((bs & (1 << (j * W + k))) && !ok[j][k]) okay = false;
            else if (bs & (1 << (j * W + k))) {
                F0R(i, W) nxt_grid[i][j][k] = 1;
            }
        }
        if (!okay) continue;
        each(edge, funY(nxt_grid, visible)) ans[edge.f] += edge.s;
    }
    return ans;
}

void computeMat(Mat& A, bool visible) {

    Cube ini(W, V<vi>(W, vi(W,0)));
    if (!idx.count(ini)) {
        idx[ini] = cnt++;
    }

    A = makeMat(sz(idx), sz(idx));
    queue<Cube> q;
    set<Cube> vis;
    vis.insert(ini);
    q.push(ini);

    bool silly = false;

    while (!q.empty()) {
        
        if (sz(idx) > 400 && !silly) {
            cout << "haha so silly :3" << endl;
            silly = true;
        }
        
        Cube cur = q.ft; q.pop();
        int u = idx[cur];
        each(nxt, funX(cur, visible)) {
            if (!idx.count(nxt.f)) {
                idx[nxt.f] = cnt++;
                F0R(i, sz(A)) A[i].pb(0);
                A.pb(vmi(sz(A[0])));
            }
            int v = idx[nxt.f];
            if (!vis.count(nxt.f)) {
                vis.insert(nxt.f);
                q.push(nxt.f);
            }
            A[v][u] += nxt.s;
        }
    }

}

/**
 * Answer should be the number in index 0 of B^3 * A^(N - 3) * I, where I is the initial vector (1,0,...,0)
 * Suppose (mu, lambda) is a cycle of the matrix found by Floyd Cycle detection for A^k * I
 * A^(N - 3) * I = A^((N - 3 - mu) % lambda) * A^mu  * I (defintion of cycle)
 * 
 * However, Floyd Cycle detection will be very slow if done in Z_10^9
 * Let (mu2, lambda2) be the cycle detected in Z_2
 * Let (mu5, lambda5) be the cycle detected in Z_5
 * Then (mu10, lambda10) = CRT((mu2, lambda2), (mu5, lambda5)) is a cycle in Z_10
 * To calculate (mu, lambda) in Z_10^9, we simply do (mu, 10^8 * lambda) (FIGURE OUT WHY XD!!!!!)
 * 
 * We can handle all of this offline! And then plug in the result:
 * 
 * (mu2, lambda2) = (3, 7)
 * (mu5, lambda5) = (0, 620)
 * (mu10, lambda10) = (3, 4340)
 * (mu, lambda) = (3, 434000000000)
 *  
*/
int solveLargeN(string const& N, Mat const& A, Mat const& B) {
	assert(false);
    bigint n = N;
    ll mu = 3, lambda = ll(7) * ll(62) * ll(MOD);
    n = n - (3 + mu); // n >>>> 6, so we can do this safely!
    n = n % lambda;
	Mat aux = pow(A, n.longValue());
	aux.resize(sz(B));
	F0R(i, sz(aux)) aux[i].resize(sz(B));
    return int((pow(B, 3) * aux)[0][0]);
}

int solveSmallN(ll N, Mat const& A, Mat const& B) {
    if (N < 3) return int(pow(B, N)[0][0]);
	Mat aux = pow(A, N - 3);
	aux.resize(sz(B));
	F0R(i, sz(aux)) aux[i].resize(sz(B));
    return int((pow(B, 3) * aux)[0][0]);
}


void printMatrix(Mat const& A) {
    int N = sz(A);
    cout << N << ' ' << N << '\n';
    F0R(i, N) {
        F0R(j, N) cout << A[i][j] << ' ';
        cout << '\n';
    }
	mi numedges = 0;
	F0R(i, N) F0R(j, N) numedges += A[i][j];
	cout << "edges -> " << numedges << '\n';
}



int main() {
    // cin.tie(0)->sync_with_stdio(0);
    Mat A, B;
    computeMat(A, true);
    // computeMat(B, false);

    // Print that matrix! yay!!!

    printMatrix(A);
    cout << "\n\n\n";
    // printMatrix(B);

    return 0;
}