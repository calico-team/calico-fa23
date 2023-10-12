#include <iostream>

using namespace std;

/**
 * When reading in values that are too large to be stored in an int, CPP tries
 * reading them anyway and results in reading wrong values and wrong answers.
 */
int solve(int A, int B) {
    // YOUR CODE HERE
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
