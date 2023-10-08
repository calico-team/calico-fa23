#include <iostream>
#include <queue>
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
    queue<ll> unshuffled;
    for (ll i = 1; i <= N; i++){
        unshuffled.push(i);
    }
    vector<ll> shuffled;
    while (!unshuffled.empty()){
        unshuffled.push(unshuffled.front());
        unshuffled.pop();
        shuffled.push_back(unshuffled.front());
        unshuffled.pop();
    }
    return find(shuffled.begin(), shuffled.end(), K)- shuffled.begin() + 1;
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
