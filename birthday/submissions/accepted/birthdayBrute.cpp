#include <iostream>
#include <math.h>  //For the pow function
using namespace std;

/**
 * TOOD: 
 * 
 * A: a non-negative integer
 */
int solve(int A) {
    // YOUR CODE HERE
    int count = 0;
    for(int i =1; i < A; i++){
        count += std::pow(i,2);
    }
    return count +3;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int A;
        cin >> A;
        cout << solve(A) << '\n';
    }
}
