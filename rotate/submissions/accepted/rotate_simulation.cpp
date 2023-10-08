#include <iostream>
#include<vector>
#include <algorithm>
#define ll long long
using namespace std;

ll solve(ll N, ll K) {
    vector<ll> deck(N);

    for (ll i= 0; i < N; i++) {
        deck[i] = i + 1;
    }
    
    for (ll i=0; i < N; i++) {
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
