#include <iostream>

using namespace std;

/**
 * Return the berkeleytime value of A.
 * 
 * A: a non-negative integer
 */
string solve(int A) {
    std::string solutionString = "berkeley";
    if (A > 180) {
        return "canceled";
    }
    for (int i = 0; i < A % 10; i++) {
        solutionString += "berkeley";
    }
    return solutionString + "time";
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
