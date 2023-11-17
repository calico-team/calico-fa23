// #include <iostream>
// #include <algorithm>
// #include <vector>

// using namespace std;

// bool dfs(int a, int b, vector<int>& S, vector<int>& A, vector<int>& B) {
//     int values[36];
//     int index = 0;
//     for (int i=0; i<a; i++) {
//         for (int j=0; j<b; j++) {
//             values[index++] = A[i] + B[j];
//         }
//     }
//     sort(values, values + index);

//     // Make sure that "values" are contained within S and keep track of the minimum m
//     // in S that hasn't been used yet.
//     int j = 0;
//     int m = 1e9;
//     for (int i=0; i<a*b; i++) {
//         while (S[j] < values[i]) m = min(m, S[j++]);
//         if (S[j] != values[i]) return false;
//         j++;
//     }
//     m = min(m, S[j]);

//     if (a == 6 && b == 6) {
//         return true;
//     }

//     if (a < 6) {
//         A[a] = m;
//         if (dfs(a+1, b, S, A, B)) return true;
//     }

//     if (b < 6) {
//         B[b] = m;
//         if (dfs(a, b+1, S, A, B)) return true;
//     }

//     return false;
// }


// void solve(vector<int>& S) {
//     int S_0 = S[0];
//     for (int i=0; i<36; i++) S[i] -= S_0;
//     vector<int> A(6, 0), B(6, 0);
//     A[1] = S[1];
//     if (dfs(2, 1, S, A, B)) {
//         for (int i=0; i < 5; i++) cout << A[i] + S_0 - 1 << ' ';
//         cout << A[5] << '\n';
//         for (int i=0; i < 5; i++) cout << B[i] + 1 << ' ';
//         cout << B[5] << '\n';
//     } else {
//         cout << "IMPOSSIBLE" << endl;
//     }
// }

// int main() {
//     int T;
//     cin >> T;
//     for (int i = 0; i < T; i++) {
//         vector<int> S(36);
//         for (int j = 0; j < 36; ++j) {
//             cin >> S[j];
//         }
//         solve(S);
//     }
// }


#include <iostream>
#include <algorithm>

using namespace std;

int T;
int S[36];
int A[6];
int B[6];

bool dfs(int a, int b) {
    int values[36];
    int index = 0;
    for (int i=0; i<a; i++) {
        for (int j=0; j<b; j++) {
            values[index++] = A[i] + B[j];
        }
    }
    sort(values, values + index);

    // Make sure that `values` are contained within S and keep track of the minimum m
    // in S that hasn't been used yet.
    int j = 0;
    int m = 1e9;
    for (int i=0; i<a*b; i++) {
        while (S[j] < values[i]) m = min(m, S[j++]);
        if (S[j] != values[i]) return false;
        j++;
    }
    m = min(m, S[j]);

    if (a == 6 && b == 6) {
        return true;
    }

    if (a < 6) {
        A[a] = m;
        if (dfs(a+1, b)) return true;
    }

    if (b < 6) {
        B[b] = m;
        if (dfs(a, b+1)) return true;
    }

    return false;
}

int main() {
    cin >> T;
    for (int t=0; t<T; t++) {
        for (int i=0; i<36; i++) cin >> S[i];

        int S_0 = S[0];
        for (int i=0; i<36; i++) S[i] -= S_0;

        A[0] = 0;
        A[1] = S[1];
        B[0] = 0;
        if (dfs(2, 1)) {
            for (int i=0; i<6; i++) cout << A[i] + S_0 - 1 << "\t";
            cout << endl;
            for (int i=0; i<6; i++) cout << B[i] + 1 << "\t";
            cout << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
}
