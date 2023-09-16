#include <iostream>

using namespace std;

/**
 * TOOD: 
 * 
 * A: a non-negative integer
 */
int solve(int A) {
    // YOUR CODE HERE

    return (A * (A-1) * (2*A -1) / 6) +3;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int A;
        cin >> A;
        cout << solve(A) << '\n';
    }
}
