#include <iostream>

using namespace std;

string feed(int);
int poop();
string guess(string);

void solve() {
    feed(1);
    feed(3);
    feed(2);
    
    int num = poop();
    if (num == 1) {
        guess("queueon");
    } else if (num == 3) {
        guess("heapeon");
    } else {
        guess("stackeon");
    }
}

string feed(int i) {
    cout << "feed " << i << endl;
    string response;
    cin >> response;
    if (response == "WRONG_ANSWER") {
        exit(0);
    }
    return response;
}

int poop() {
    cout << "poop" << endl;
    string response;
    cin >> response;
    if (response == "WRONG_ANSWER") {
        exit(0);
    }
    return stoi(response);
}

string guess(string s) {
    cout << "guess " << s << endl;
    string response;
    cin >> response;
    if (response == "WRONG_ANSWER") {
        exit(0);
    }
    return response;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        solve();
    }
    return 0;
}
