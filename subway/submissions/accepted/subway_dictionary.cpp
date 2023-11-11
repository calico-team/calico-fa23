#include <bits/stdc++.h>
using namespace std;

using ll = long long;

/**
 * Find the total distance the subway must travel until all passengers have
 * arrived at their ending station.
 * 
 * N: the number of passengers
 * M: the number of stations
 * K: the maximum number of passengers the subway can carry
 * S: list of starting stations for each passenger
 * E: list of ending stations for each passenger
 * P: list of positions in line at their starting station for each passenger
 */
ll solve(int N, int M, int K, vector<int> &S, vector<int> &E, vector<int> &P) {
    
    map<int, vector<int>> shit_format;
    for (int i = 0; i < N; ++i) {
        if (shit_format[--S[i]].size() < P[i])
            shit_format[S[i]].resize(P[i]);
        shit_format[S[i]][--P[i]] = --E[i];
    }
    
    map<int, queue<int>> stations;
    for (auto& station : shit_format)
        for (int depressed_comuter : station.second)
            stations[station.first].push(depressed_comuter);

    priority_queue<ll, vector<ll>, greater<ll>> soobway;
    ll t = 0;
    while (!stations.empty()) {
        if (soobway.size() == K) {
            // If soobway is full, we need to find the next stop
            t = soobway.top(); soobway.pop();
        }
        else {
            // Next station with passengers that we visit is the lower bound of t % M
            auto next_station = stations.lower_bound(t % M);
            // If there is no station after, just advance until the first one and repeat the process
            if (next_station == stations.end()) {
                t = t / M * M + M;
                continue;
            }
            int e = next_station->first;
            // Set t = min{ j >= t | j % M = e }
            if (t % M <= e) t = t + e - t % M;
            else t = t + M + e - t % M;

            // All passengers up to this point can go down.
            while (!soobway.empty() && soobway.top() <= t) soobway.pop();

            // Add the station they need to get down to the priority queue
            int s = next_station->second.front();
            next_station->second.pop();
            if (next_station->second.empty()) // Erase the station if there are no passangers left
                stations.erase(next_station);
            
            // insert { min j >= t | j % M = s }
            if (e <= s) soobway.push(t + s - e);
            else soobway.push(t + M + s - e);
        }
    }

    while (!soobway.empty()) t = soobway.top(), soobway.pop();

    return t;

}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, M, K;
        cin >> N >> M >> K;
        vector<int> S(N);
        for (int &item : S) {
            cin >> item;
        }
        vector<int> E(N);
        for (int &item : E) {
            cin >> item;
        }
        vector<int> P(N);
        for (int &item : P) {
            cin >> item;
        }
        cout << solve(N, M, K, S, E, P) << '\n';
    }
}
