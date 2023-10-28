#include <iostream>
#include <vector>

using namespace std;

bool next_combination(vector<int>& a, int n) {
    int k = (int)a.size();
    for (int i = k - 1; i >= 0; i--) {
        if (a[i] < n - k + i + 1) {
            a[i]++;
            for (int j = i + 1; j < k; j++)
                a[j] = a[j - 1] + 1;
            return true;
        }
    }
    return false;
}

bool check(vector<int>& comb, vector<int>& S, vector<int>& D1, vector<int>& D2) {
    D1.assign(6, 0);
    D2.assign(6, 0);
    D1[0] = 1;
    D2[0] = S[0] - 1;
    for (int i = 0; i < 5; ++i)
        D2[i + 1] = S[comb[i]];
    
}

void solve(vector<int>& S) {
    vector<int> D1(6), D2(6);
    D1[0] = 1; D2[0] = S[0] - 1;
    vector<int> comb(5);
    for (int i = 0; i < 5; ++i) comb[i] = i + 1;
    do {
        if (check(comb, S, D1, D2)) {

        }
    } while (next_combination(comb, 30));
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
