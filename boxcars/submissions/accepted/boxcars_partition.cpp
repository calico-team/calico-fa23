#include <iostream>
#include <vector>
#include <set>

using namespace std;

template <typename T> ostream& operator << (ostream& o, vector<T> const& v) {
    for (int i = 0; i < int(v.size()) - 1; ++i) o << v[i] << ' ';
    if (!v.empty()) o << v.back();
    return o;
}

bool check(vector<int> const& S, vector<int>& a, vector<int>& b) {
    vector<int> comb(4);
    for (comb[0] = 2; comb[0] <= 30; ++comb[0]) {
        for (comb[1] = comb[0] + 1; comb[1] <= 30; ++comb[1]) {
            for (comb[2] = comb[1] + 1; comb[2] <= 30; ++comb[2]) {
                for (comb[3] = comb[2] + 1; comb[3] <= 30; ++comb[3]) {


                    multiset<int> remaining;
                    for (int i = 2; i < 36; ++i) {
                        bool add = true;
                        for (int j = 0; j < 4; ++j) if (comb[j] == i) add = false;
                        if (add) remaining.insert(S[i]);
                    }

                    
                    for (int i = 2; i < 6; ++i) a[i] = S[comb[i - 2]] - b[0];

                    bool ok = true;

                    for (int j = 1; j < 6 && ok; ++j) {
                        b[j] = *remaining.begin() - a[0];
                        for (int i = 0; i < 6 && ok; ++i) {
                            auto it = remaining.find(a[i] + b[j]);
                            if (it == remaining.end()) ok = false;
                            else remaining.erase(it);
                        }
                    }

                    if (ok) return true;


                }
            }
        }
    }

    return false;
    
}

void solve(vector<int>& S) {
    vector<int> a, b;
    a = { 1, S[1] - S[0] + 1, 0, 0, 0, 0};
    b = { S[0] - 1, 0, 0, 0, 0, 0 };
    if (check(S, a, b)) {
        cout << a << '\n' << b << '\n';
        return;
    }
    a = { S[0] - 1, S[1] - 1, 0, 0, 0, 0 };
    b = { 1, 0, 0, 0, 0, 0 };
    if (check(S, a, b)) {
        cout << a << '\n' << b << '\n';
        return ;
    }
    cout << "IMPOSSIBLE\n";
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
