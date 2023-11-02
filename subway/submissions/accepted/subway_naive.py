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
    
    passengers_delivered, total_dist, cur_station = 0, 0, 0
    train = []
    while passengers_delivered < N:
        total_dist += 1
        
        new_train = []
        for passenger_end in train:
            if passenger_end == cur_station:
                passengers_delivered += 1
            else:
                new_train.append(passenger_end)
        train = new_train

        while len(stations[cur_station]) > 0 and len(train) < K:
            new_train.append(stations[cur_station].pop(0))
        
        cur_station = (cur_station + 1) % M
    
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