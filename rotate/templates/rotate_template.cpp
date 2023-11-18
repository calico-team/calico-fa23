#include <iostream>

using namespace std;

/**
 * Return the position of the card labelled K after shuffling a deck with N
 * cards, where the topmost card is in position 1, the second from topmost card
 * is position 2, and so on.
 * 
 * N: the number of cards in the deck
 * K: the label of the target card
 */
int solve(int N, int K) {
    // YOUR CODE HERE
    return 0;
}

int main() {
    int T;
    int N, K;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N >> K;
        cout << solve(N, K) << '\n';
    }
}
