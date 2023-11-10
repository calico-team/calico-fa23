#include <iostream>

using namespace std;

string feed(int);
int poop();
string guess(string);

/**
 * Identify the unknown datamon through making feed and poop queries.
 *  
 * Call the feed and poop functions below to make feed and poop queries. Return
 * from this function after calling the guess function to make a guess query.
 */
void solve() {
    // YOUR CODE HERE
}

/*
 * Feed a number to the Datamon. Returns OK if successful.
 */
string feed(int i) {
    cout << "feed " << i << endl;
    string response;
    cin >> response;
    if (response == "WRONG_ANSWER") {
        exit(0);
    }
    return response;
}

/*
 * Get the Datamon to poop out a number. Returns the number pooped out.
 */
int poop() {
    cout << "poop" << endl;
    string response;
    cin >> response;
    if (response == "WRONG_ANSWER") {
        exit(0);
    }
    return stoi(response);
}

/*
 * Guess the species of the Datamon and end this test case. Returns CORRECT if
 * the guess is correct. Exits otherwise.
 */
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
