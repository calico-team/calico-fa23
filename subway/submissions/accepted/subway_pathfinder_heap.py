import heapq
import time

class Pathfinder:
    """
    TODO explain how this hot garbage works
    """
    
    def __init__(self, sorted_stations, is_good):
        self.is_good = is_good
        
        self.next_station = {}
        for station, next in zip(sorted_stations, sorted_stations[1:]):
            self.next_station[station] = next
        self.next_station[sorted_stations[-1]] = sorted_stations[0]
    
    def find(self, x):
        if not self.is_good(self.next_station[x]):
            self.next_station[x] = self.find(self.next_station[x])
        return self.next_station[x]


def solve(N: int, M: int, K: int, S: list[int], E: list[int], P: list[int]) -> int:
    stations = {s: [] for s in S}
    for s, e, p in zip(S, E, P):
        stations[s].extend([None] * (p - len(stations[s])))
        stations[s][p - 1] = e
    for station in stations.values():
        station.reverse()
    
    pathfinder = Pathfinder(sorted(set(S + E)), stations.get)
    train_heap = []
    
    curr_station = min(set(S))
    total_dist = curr_station - 1
    passengers_delivered = 0
    while passengers_delivered < N:
        while train_heap and train_heap[0][0] == total_dist:
            heapq.heappop(train_heap)
            passengers_delivered += 1
        while curr_station in stations and stations[curr_station] and len(train_heap) < K:
            e = stations[curr_station].pop()
            heapq.heappush(train_heap, (total_dist + dist(curr_station, e, M), e))
        if curr_station in stations and not stations[curr_station]:
            stations.pop(curr_station)
        
        next_pick_up_station = next_drop_off_station = curr_station
        if stations:
            next_pick_up_station = pathfinder.find(curr_station)
            next_pick_up_dist = dist(curr_station, next_pick_up_station, M)
        if train_heap:
            next_drop_off_station = train_heap[0][1]
            next_drop_off_dist = train_heap[0][0] - total_dist
        
        if len(train_heap) == K or not stations:
            next_station = next_drop_off_station
        elif not train_heap:
            next_station = next_pick_up_station
        elif train_heap and stations:
            if next_drop_off_dist < next_pick_up_dist:
                next_station = next_drop_off_station
            else:
                next_station = next_pick_up_station
        
        if next_station:
            total_dist += dist(curr_station, next_station, M)
            curr_station = next_station
    
    return total_dist


def dist(a, b, M):
    return (b - a) % M


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
