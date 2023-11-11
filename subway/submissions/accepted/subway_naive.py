def solve(N: int, M: int, K: int, S: list[int], E: list[int], P: list[int]) -> int:
    stations = [[] for _ in range(M)]
    for start, end, pos in zip(S, E, P):
        station = stations[start - 1]
        while len(station) < pos:
            station.append(None)
        station[pos - 1] = end - 1
    
    passengers_delivered, total_dist, cur_station = 0, 0, 1
    train = []
    while passengers_delivered < N:
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
        total_dist += 1
    
    return total_dist


def main():
    T = int(input())
    for _ in range(T):
        N, M, K = [int(x) for x in input().split()]
        
        S = [int(x) for x in input().split()]
        E = [int(x) for x in input().split()]
        P = [int(x) for x in input().split()]
        
        print(solve(N, M, K, S, E, P))


if __name__ == '__main__':
    main()