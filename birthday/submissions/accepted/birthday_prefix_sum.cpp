#include <iostream>
#include <vector>
using namespace std;

using ll = long long;

int main() {
    int T;
    cin >> T;
    vector<ll> ans(3E6);
    ans[0] = 3;
    for (int i = 1; i < 3E6; ++i) ans[i] = ans[i-1] + ll(i) * ll(i);
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        cout << ans[N-1] << '\n';
    }
}
