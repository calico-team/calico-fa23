#include <iostream>
#include <vector>

using namespace std;

/**
 * Output two lines containing the sides of the dice separated by dashes -,
 * such that the two dice yield the given sum distribution S.
 * 
 * S: a list containing the possible 36 sums achieved rolling the two unknown die.
 */
void solve(vector<int>& S) {
    // YOUR CODE HERE
    return;
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
