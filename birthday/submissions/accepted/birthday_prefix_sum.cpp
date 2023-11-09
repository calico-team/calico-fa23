#include <iostream>
#include <vector>
using namespace std;

using ll = long long;

int main() {
    int T;
    cin >> T;
    vector<ll> ans(3E6+1);
    for (int i = 1; i < 3E6+1; ++i) ans[i] = ans[i-1] + ll(i) * ll(i);
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        cout << ans[N] - N << '\n';
    }
    return 0;
}
