#include <iostream>

using namespace std;

/**
 * Implements addition with CPP's fixed precision int. This passes the main test
 * set only.
 */
int solve(int A, int B) {
    return A + B;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int A, B;
        cin >> A >> B;
        cout << solve(A, B) << '\n';
    }
}
