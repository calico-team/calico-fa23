#include <iostream>

using namespace std;

/**
 * Return the number of possible towers that Big Ben can build with N blocks.
 * 
 * @param N : number of 1x1x3 Benga Bricks we can use to construct the Benga tower.
 */
int solve(long long N) {
    // YOUR CODE HERE
    return -1;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        long long N;
        cin >> N; // CAUTION! For the last Bonus you might want to change this.
        cout << solve(N) << '\n';
    }
}
