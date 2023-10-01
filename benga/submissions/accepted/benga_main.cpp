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


const int MOD = 1E9;


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


// Actual Benga

const int WIDTH = 4;

map<V<vi>, int> idx;
int cnt = 0;

V<V<vi>> funY(V<vi> grid, bool letMiddleBlocks) {
    // Try placing horizontal blocks that go through the Y coordinate
    V<V<vi>> ans;
    vb ok(WIDTH, true);
    F0R(i, WIDTH) F0R(j, WIDTH) if (grid[i][j]) ok[j] = false;
    F0R(bs, 1 << WIDTH) {
        bool okay = true;
        V<vi> nxt_grid = grid;
        F0R(j, WIDTH)
            if ((bs & (1 << j)) && !ok[j]) okay = false;
            else if (bs & (1 << j)) F0R(i, WIDTH) nxt_grid[i][j] = 1;
        
        if (!letMiddleBlocks)
            FOR(i, 1, WIDTH - 1)
                FOR(j, 1, WIDTH - 1)
                    if (!nxt_grid[i][j])
                        okay = false;

        if (!okay) continue;
        // The only option left is to place vertical tiles in the empty spots
        // Place vertical in empty and cut the bottom part
        F0R(i, WIDTH) F0R(j, WIDTH) nxt_grid[i][j] = (nxt_grid[i][j] + WIDTH - 1) % WIDTH;
        ans.pb(nxt_grid);
    }
    return ans;
}

V<V<vi>> funX(V<vi> grid, bool letMiddleBlocks) {
    // Try placing horizontal blocks that go through the X coordinate
    V<V<vi>> ans;
    vb ok(WIDTH, true);
    F0R(i, WIDTH) F0R(j, WIDTH) if (grid[i][j]) ok[i] = false;
    F0R(bs, 1 << WIDTH) {
        bool okay = true;
        V<vi> nxt_grid = grid; // We will place the tiles in this grid
        F0R(i, WIDTH)
            if ((bs & (1 << i)) && !ok[i]) okay = false;
            else if (bs & (1 << i)) F0R(j, WIDTH) nxt_grid[i][j] = 1; // Place horizontal tile
        if (!okay) continue;
        each(adjacent_state, funY(nxt_grid, letMiddleBlocks))
            ans.pb(adjacent_state);
    }
    return ans;
}

void computeMat(Mat& A, bool letMiddleBlocks) {

    V<vi> ini(WIDTH, vi(WIDTH, 0));

    if (!idx.count(ini)) {
        idx[ini] = cnt++;
    }

    A = makeMat(sz(idx), sz(idx));
    // Run a BFS algorithm to calculate all reachable states from the initial state
    queue<V<vi>> q;
    set<V<vi>> vis;
    vis.insert(ini);
    q.push(ini);

    while (!q.empty()) {
        V<vi> cur = q.ft; q.pop();
        int u = idx[cur];
        each(nxt, funX(cur, letMiddleBlocks)) {
            if (!idx.count(nxt)) { 
                idx[nxt] = cnt++;
                // Increase matrix size
                F0R(i, sz(A)) A[i].pb(0);
                A.pb(vmi(sz(A[0])));
            }
            int v = idx[nxt];
            if (!vis.count(nxt)) { vis.insert(nxt); q.push(nxt); }
            A[v][u] += 1;
        }
    }
}

int solveSmallN(ll N, Mat const& A, Mat const& B) {
    if (N <= 3) return int(pow(B, N)[0][0]);
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

    cin.tie(0)->sync_with_stdio(0);

    Mat A, B;
    computeMat(A, false);
    computeMat(B, true);

    vi first_cases = { 1, 2, 4, 21 };

    B *= B; B *= B; // check if this works??????????? it should!

    B.rsz(sz(A));
    F0R(i, sz(B)) B[i].rsz(sz(A));

	int TC;
	cin >> TC;
	while (TC--) {
		ll N; cin >> N;
        if (N <= 3) cout << first_cases[N] << '\n';
		else cout << solveSmallN(N, A, B) << '\n';
	}

    return 0;
}