#include <iostream>
#include<vector>
#include <algorithm>
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
    vector<ll> deck(N);

    for (ll i= 0; i < N; i++){
        deck[i] = i + 1;
    }
    
    for (ll i=0; i < N; i++){
        int card = deck[i];
        deck.erase(deck.begin() + i, deck.begin() + i + 1);
        deck.push_back(card);
    }
    
    return find(deck.begin(), deck.end(), K) - deck.begin() + 1;  
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
