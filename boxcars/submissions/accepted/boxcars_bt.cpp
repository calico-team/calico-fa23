#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool backtrack(vector<int> const& S, vector<int>& A, vector<int>& B) {
    vector<int> values;
    for (int a : A) for (int b : B) values.push_back(a + b);
    sort(values.begin(), values.end());
    int j = 0, m = 1E9;
    int a = A.size(), b = B.size();
    for (int i = 0; i < values.size(); ++i) {
        while (j < 36 && S[j] < values[i]) m = min(m, S[j++]);
        if (j >= 36 || S[j] != values[i]) return false;
        ++j;
    }
    if (j < 36) m = min(m, S[j]);
    if (a == 6 && b == 6) return true;
    if (a < 6) {
        A.push_back(m);
        if (backtrack(S, A, B)) return true;
        A.pop_back();
    }
    if (b < 6) {
        B.push_back(m);
        if (backtrack(S, A, B)) return true;
        B.pop_back();
    }
    return false;
}

/**
 * Output two lines containing the faces of the dice separated by spaces,
 * such that the sorted list of their pairwise sums is equal to S.
 * 
 * S: the list containing the desired nondecreasing list of 36 pairwise sums
 */
void solve(vector<int>& S) {
    int S_0 = S[0];
    for (int& s : S) s -= S_0;
    // for (int s : S) cerr << s << ' ';
    // cerr << endl;
    vector<int> A = { 0, S[1] }, B = { 0 };
    if (backtrack(S, A, B)) {
        for (int i = 0; i < 5; ++i) cout << A[i] + S_0 - 1 << ' ';
        cout << A.back() + S_0 - 1 << '\n';
        for (int i = 0; i < 5; ++i) cout << B[i] + 1 << ' ';
        cout << B.back() + 1 << '\n';
    } else {
        cout << "IMPOSSIBLE\n";
    }
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        vector<int> S(36);
        for (int j = 0; j < 36; ++j) {
            cin >> S[j];
        }
        solve(S);
    }
}
