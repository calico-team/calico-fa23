#include <iostream>

#define ll long long

using namespace std;

/**
 * Return the position of the card labelled K after shuffling a deck with N
 * cards.
 * 
 * N: the number of cards in the deck
 * K: the label of the target card
 */
ll solve(ll N, ll K) {
    // YOUR CODE HERE
    if (N % 2 == 0){
        if (K % 2 == 0){
            return K / 2;
        }
        return N / 2 + solve(N / 2, K / 2 + 1);
    }
    else {
        if (K % 2 == 0){
            return K / 2;
        }
        if (K == 1){
            return N / 2 + 1;
        }
        return N / 2 + 1 + solve(N / 2, K / 2);
    }
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
