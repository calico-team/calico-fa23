#include <iostream>
#include <vector>

using namespace std;

/**
 * Output two lines containing the faces of the dice separated by spaces,
 * such that the sorted list of their pairwise sums is equal to S.
 * 
 * S: the list containing the desired nondecreasing list of 36 pairwise sums
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
