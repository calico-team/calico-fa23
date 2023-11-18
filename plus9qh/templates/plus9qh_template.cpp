#include <iostream>
#include <vector>

using namespace std;

/**
 * Find an HQ9+ program that outputs exactly the given text or return IMPOSSIBLE
 * if no solutions exist.
 * 
 * N: the number of lines of text
 * X: a list containing the lines of the text
 */
string solve(int N, vector<string> &X) {
    // YOUR CODE HERE
    return "";
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        cin.get();
        vector<string> X(N);
        for (int j = 0; j < N; j++) {
            getline(cin, X[j]);
        }
        cout << solve(N, X) << '\n';
    }
}
