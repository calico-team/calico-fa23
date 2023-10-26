#include <iostream>
#include <vector>

using namespace std;

const string HELLO_WORLD = "Hello, world!";
const string LYRICS[6] = {
    "99 bottles of beer on the wall, 99 bottles of beer.",
    "Take one down and pass it around, 98 bottles of beer on the wall.",
    "98 bottles of beer on the wall, 98 bottles of beer.",
    "Take one down and pass it around, 97 bottles of beer on the wall.",
    "97 bottles of beer on the wall, 97 bottles of beer.",
    "Take one down and pass it around, 96 bottles of beer on the wall."
};
string CORRECT = "+9QH";

string solve(int N, vector<string> X) {
    bool okay = true;
    string quine = "";
    string ans = "";
    for (int i = 0; i < N; ++i) {
        bool beer = false;
        if (i + 6 <= N) {
            beer = true;
            for (int j = 0; j < 6; ++j) {
                if (X[i + j] != LYRICS[j]) {
                    beer = false;
                }
            }
        }
        if (beer) {
            ans.push_back('9');
            i += 5;
        } else if (X[i] == HELLO_WORLD) {
            ans.push_back('H');
        } else if (!quine.empty() && quine != X[i]) { 
            okay = false;
        } else {
            quine = X[i];
            ans.push_back('Q');
        }
    }
    string clean_program = "";
    for (char c : quine) {
        if (CORRECT.find(c) == string::npos) {
            okay = false;
        } else if (c != '+') {
            clean_program.push_back(c);
        }
    }
    if (!quine.empty() && clean_program != ans) {
        okay = false;
    }
    if (!quine.empty()) {
        ans = quine;
    }
    return okay ? ans : "IMPOSSIBLE";
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N; cin.get();
        vector<string> X(N);
        for (int j = 0; j < N; j++) {
            getline(cin, X[j]);
        }
        cout << solve(N, X) << '\n';
    }
}
