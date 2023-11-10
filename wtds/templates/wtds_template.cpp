#include <cassert>
#include <iostream>
#include <vector>

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
 * Feed a number to the Datamon.
 */
string feed(int i){
    cout << "feed " << i << endl;
    string response;
    cin >> response;
    return response;
}

/*
 * Get the Datamon to poop out a number.
 */
int poop(){
    cout << "poop" << endl;
    int response;
    cin >> response;
    return response;
}

/*
 * Guess the species of the Datamon and end this test case.
 */
string guess(string s){
    cout << "guess " << s << endl;
    string response;
    cin >> response;
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
