def solve(N: int, M: int, K: int, S: list[int], E: list[int]) -> int:
    unique_starts = set(S)
    unique_ends = set(E)
    waiting = {i: [] for i in unique_starts}
    all_stations = sorted(set(S + E))

    passengers_left = N
    pointer = -1
    distance = 0
    last_visited = 0

    train = {i: 0 for i in set(E)}
    open_seats = K
    
    for s, e in zip(S, E):
        waiting[s].append(e)
    for station in waiting.values():
        station.reverse()

    while passengers_left > 0:
        pointer = (pointer + 1) % len(all_stations)
        this_station = all_stations[pointer]

        if this_station in unique_ends:
            open_seats += train[this_station] # let passengers off first
            passengers_left -= train[this_station] 
            train[this_station] = 0

        if this_station in unique_starts:
            while open_seats > 0 and waiting[this_station]: # new passengers board
                next_to_add = waiting[this_station].pop(0)
                train[next_to_add] += 1
                open_seats -= 1

        distance += ((this_station - last_visited) % M)
        last_visited = this_station

    return distance
    

def main():
    T = int(input())
    for _ in range(T):
        N, M, K = [int(x) for x in input().split()]
        S = [int(x) for x in input().split()]
        E = [int(x) for x in input().split()]
        print(solve(N, M, K, S, E))


if __name__ == '__main__':
    main()
