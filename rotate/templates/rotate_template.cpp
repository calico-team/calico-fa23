#include <iostream>

using namespace std;

typedef long long ll;

/**
 * Return the position of the card labelled K after shuffling a deck with N
 * cards.
 * 
 * N: the number of cards in the deck
 * K: the label of the target card
 */
ll solve(ll N, ll K) {
    // YOUR CODE HERE
    return 0;
}

int main() {
    int T;
    ll N, K;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N >> K;
        cout << solve(N, K) << '\n';
    }
}
