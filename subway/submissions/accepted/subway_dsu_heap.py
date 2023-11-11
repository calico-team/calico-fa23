import heapq
import time

class StationFinder:
    """
    A DSU-like data structure that represents a set of cyclically numbered
    stations and a subset of start stations. Supports the following queries:
    - find(x): Find the nearest start station after station x.
    - remove_start(x): Remove station x from the set of start stations.
    """
    
    def __init__(self, S, E):
        sorted_stations = sorted(set(S + E + [1]))
        self.next_station = {}
        for i in range(len(sorted_stations)):
            self.next_station[sorted_stations[i - 1]] = sorted_stations[i]
        
        self.start_set = set(S)
    
    def find(self, x):
        if self.next_station[x] not in self.start_set:
            self.next_station[x] = self.find(self.next_station[x])
        return self.next_station[x]
    
    def remove_start(self, x):
        if x in self.start_set:
            self.start_set.remove(x)
    
    def __len__(self):
        return len(self.start_set)


class Subway:
    """
    Represents the subway using a min heap of passengers and other auxiliary
    variables to track the current station and total travelled distance.
    - exit_passenger(): Attempts to let a passenger exit at the current station.
      Returns True if successful and False otherwise.
    - enter_passenger(station_list): Attempts to let a passenger enter from the
      given station list. Returns True if successful and False otherwise.
    """
    
    def __init__(self, K, M):
        self.K = K
        self.M = M
        self.passengers = []
        self.curr_station = 1
        self.total_dist = 0
    
    def exit_passenger(self):
        if self.passengers:
            ending_dist, ending_station = self.passengers[0]
            if ending_dist == self.total_dist:
                heapq.heappop(self.passengers)
                return True
        return False
    
    def enter_passenger(self, station_list):
        if len(self.passengers) < self.K and len(station_list) > 0:
            ending_station = station_list.pop()
            delta = dist(self.curr_station, ending_station, self.M)
            ending_dist = self.total_dist + delta
            heapq.heappush(self.passengers, (ending_dist, ending_station))
            return True
        return False
    
    def peek(self):
        return self.passengers[0]
    
    def __len__(self):
        return len(self.passengers)


def solve(N: int, M: int, K: int, S: list[int], E: list[int]) -> int:
    stations = {station: [] for station in S + E + [1]}
    for s, e in zip(S, E):
        stations[s].append(e)
    for station in stations.values():
        station.reverse()
    
    finder = StationFinder(S, E)
    subway = Subway(K, M)
    
    while True:
        while subway.exit_passenger():
            pass
        
        while subway.enter_passenger(stations[subway.curr_station]):
            pass
        if not stations[subway.curr_station]:
            finder.remove_start(subway.curr_station)
        
        if len(finder) > 0:
            next_pick_up_station = finder.find(subway.curr_station)
            next_pick_up_dist = dist(subway.curr_station, next_pick_up_station, M)
        if len(subway) > 0:
            next_drop_off_total, next_drop_off_station = subway.peek()
            next_drop_off_dist = next_drop_off_total - subway.total_dist
        next_station = None
        
        if len(finder) > 0 or len(subway) > 0:
            if len(finder) == 0 or len(subway) == K:
                next_station = next_drop_off_station
            elif len(subway) == 0:
                next_station = next_pick_up_station
            else:
                if next_drop_off_dist < next_pick_up_dist:
                    next_station = next_drop_off_station
                else:
                    next_station = next_pick_up_station
            
            subway.total_dist += dist(subway.curr_station, next_station, M)
            subway.curr_station = next_station
        else:
            break
    
    return subway.total_dist


def dist(a, b, M):
    return (b - a) % M


def main():
    T = int(input())
    for _ in range(T):
        N, M, K = [int(x) for x in input().split()]
        S = [int(x) for x in input().split()]
        E = [int(x) for x in input().split()]
        print(solve(N, M, K, S, E))


if __name__ == '__main__':
    main()
