def solve(N: int, M: int, K: int, S: list[int], E: list[int]) -> int:
    stations = [[] for _ in range(M + 1)]
    for s, e in zip(S, E):
        stations[s].append(e)
    
    passengers_done, total_dist, curr_station = 0, 0, 1
    train = []
    while True:
        while curr_station in train:
            train.remove(curr_station)
            passengers_done += 1
        
        while stations[curr_station] and len(train) < K:
            train.append(stations[curr_station].pop(0))
        
        if passengers_done < N:
            curr_station = curr_station % M + 1
            total_dist += 1
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
