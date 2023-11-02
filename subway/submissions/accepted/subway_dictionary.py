from collections import defaultdict

def solve(N: int, M: int, K: int, S: list[int], E: list[int], P: list[int]) -> int:
    """
    Find the distance the subway must travel before all passengers
    arrive at their ending station

    N: the number of passengers
    M: the number of stations
    K: the capacity of the train
    S: the list of starting stations for each passenger
    E: the list of ending stations for each passenger
    P: the list of line positions for each passenger at their station
    """
    stations = [[] for _ in range(M)]
    for start, end, pos in zip(S, E, P):
        station = stations[start - 1]
        while len(station) < pos:
            station.append(None)
        station[pos - 1] = end - 1
    
    stations = [station[::-1] for station in stations]
    
    train = defaultdict(lambda : 0)
    train_occupancy = 0
    passengers_delivered, total_dist, cur_station = 0, 0, 0
    while passengers_delivered < N:
        train_occupancy -= train[cur_station]
        passengers_delivered += train[cur_station]
        train[cur_station] = 0

        while len(stations[cur_station]) > 0 and train_occupancy < K:
            train[stations[cur_station].pop()] += 1
            train_occupancy += 1
        
        cur_station = (cur_station + 1) % M
        total_dist += 1
    
    return total_dist


def main():
    T = int(input())
    for _ in range(T):
        info = input().split(' ')
        N, M, K = int(info[0]), int(info[1]), int(info[2])
        S = [int(x) for x in input().split(' ')]
        E = [int(x) for x in input().split(' ')]
        P = [int(x) for x in input().split(' ')]
        solve(N, M, K, S, E, P)


if __name__ == '__main__':
    main()