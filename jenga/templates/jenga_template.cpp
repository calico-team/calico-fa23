#include <iostream>

using namespace std;

typedef long long ll;

/**
* Return the number of unique Jenga towers that can be built using N or fewer
* bricks. Give your answer modulo 3359232.
* 
* N: the maximum number of bricks to use
*/
int solve(ll N) {
    // YOUR CODE HERE
    return -1;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        ll N;
        cin >> N;
        cout << solve(N) << '\n';
    }
}