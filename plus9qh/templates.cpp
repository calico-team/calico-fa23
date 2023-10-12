#include <iostream>
#include <vector>

using namespace std;

/**
    Output a program that outputs the given text.

    T: the number of Test Cases
    N: the number of lines in the program
    X: the list of lines of the program
 */
void solve(int N, vector<int> X) {
    // YOUR CODE HERE
    return;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        vector<int> X(N);
        for (int j = 0; j < N; j++) {
            cin >> X[j];
        }
        solve(N, X);
    }
}