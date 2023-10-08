#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int solve(int N, int K) {
    vector<int> deck(N);
    for (int i = 1; i <= N; i++) {
        deck[i] = i;
    }
    
    for (int i = 0; i < N; i++) {
        int card = deck[i];
        deck.erase(deck.begin() + i);
        deck.push_back(card);
    }
    
    return find(deck.begin(), deck.end(), K) - deck.begin() + 1;  
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
