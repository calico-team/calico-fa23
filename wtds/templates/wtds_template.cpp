#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

vector<int> draw();
string check(int);

/*
 * Find the unknown datamon through feed, poop, and guess queries.
    
 * Call the feed, poop, and guess functions below to make feed, poop, and guess queries.
*/
void solve() {
    // YOUR CODE HERE
}

/*
 * Feed the datamon an integer
*/
string feed(int i){
    cout << "feed " << i << endl;
    string result;
    cin >> result;
    return result;
}

/*
 * Datamon poops out an integer depending on its species 
*/
int poop(){
    cout << "poop" << endl;
    int result;
    cin >> result;
    return result;
}

/*
 * Guess the datamon 
*/
string guess(string i){
    cout << "guess " << i << endl;
    string result;
    cin >> result;
    return result;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        solve();
    }
    string temp;
    cin >> temp;
}