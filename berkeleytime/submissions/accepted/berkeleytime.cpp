#include <iostream>

using namespace std;

string solve(int N) {
    if (N == 0) {
        return "haha good one";
    } else if (N >= 180) {
        return "canceled";
    } else {
        string berkeleys = "";
        for (int i = 0; i < N; i += 10) {
            berkeleys += "berkeley";
        }
        return berkeleys + "time";
    }
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        cout << solve(N) << '\n';
    }
}
