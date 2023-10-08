#include <iostream>
#include <queue>
#include<vector>
#include <algorithm>
#define ll long long
using namespace std;

ll solve(ll N, ll K) {
    queue<ll> unshuffled;
    vector<ll> shuffled;
    for (ll i = 1; i <= N; i++) {
        unshuffled.push(i);
    }
   
    while (!unshuffled.empty()) {
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
