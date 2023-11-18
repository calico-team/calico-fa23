def solve(N: int, M: int, K: int, S: list[int], E: list[int]) -> int:
    stations = {station: [] for station in S + E + [1]}
    for s, e in zip(S, E):
        stations[s].append(e)
    for station in stations.values():
        station.reverse()
    
    all_stations = sorted(set(S + E + [1]))
    curr_station_idx = 0

    passengers_done, total_dist = 0, 0
    train, open_seats = {i: 0 for i in set(E)}, K
    while True:
        curr_station = all_stations[curr_station_idx]
        
        if curr_station in train:
            open_seats += train[curr_station]
            passengers_done += train[curr_station]
            train[curr_station] = 0

        while open_seats > 0 and stations[curr_station]:
            next_to_add = stations[curr_station].pop()
            train[next_to_add] += 1
            open_seats -= 1
        
        if passengers_done < N:
            next_station_idx = (curr_station_idx + 1) % len(all_stations)
            total_dist += (all_stations[next_station_idx] - curr_station) % M
            curr_station_idx = next_station_idx
        else:
            break

    return total_dist
    

def main():
    T = int(input())
    for _ in range(T):
        N, M, K = [int(x) for x in input().split()]
        S = [int(x) for x in input().split()]
        E = [int(x) for x in input().split()]
        print(solve(N, M, K, S, E))


if __name__ == '__main__':
    main()
