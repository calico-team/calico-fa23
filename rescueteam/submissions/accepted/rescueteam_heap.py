import collections
import heapq


def solve(F: int, B: int, N: int, M: int, S: int, E: int, X: list[int], Y: list[int], K: list[int]):
    
    dungeon = [[] for _ in range(N + 1)]
    for x, y in zip(X, Y):
        dungeon[x].append(y)
        dungeon[y].append(x)
    
    def bfs_dists(graph, start):
        dists = [float('inf') for _ in graph]
        curr_dist = 0
        visited = [False] * len(graph)
        visited[start] = True
        queue = collections.deque([start])
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                dists[curr] = curr_dist
                for adj in graph[curr]:
                    if not visited[adj]:
                        queue.append(adj)
                        visited[adj] = True
            curr_dist += 1
        return dists
    
    start_dists = bfs_dists(dungeon, S)
    end_dists = bfs_dists(dungeon, E)
    skip_dist = start_dists[E]
    treasure_deltas = [start_dists[i] + end_dists[i] - skip_dist for i in range(N + 1)]
    
    curr_belly = 0
    selected_treasure_deltas = []
    best_treasures = 0
    # invariant: iteration i gives the best treasures if we exit floor i
    for k in K:
        # we always need to include skip_dist, so remove prior treasures if
        # necessary to allow us to get here in the first place
        while selected_treasure_deltas and curr_belly + skip_dist > B:
            curr_belly -= -heapq.heappop(selected_treasure_deltas)
        if curr_belly + skip_dist > B:
            # we can't get through this floor, no need to keep looking
            break
        curr_belly += skip_dist
        
        # consider picking up the treasure on this floor
        curr_treasure_delta = treasure_deltas[k]
        if curr_belly + curr_treasure_delta <= B:
            # if we can pick it up at no cost, its always optimal to pick it up
            heapq.heappush(selected_treasure_deltas, -curr_treasure_delta)
            curr_belly += curr_treasure_delta
        else:
            # if it's too expensive, see if we can trade for it
            if len(selected_treasure_deltas) > 0 and curr_treasure_delta < -selected_treasure_deltas[0]:
                # trading is only worth it if it's cheaper than our 
                curr_belly -= -heapq.heappop(selected_treasure_deltas)
                heapq.heappush(selected_treasure_deltas, -curr_treasure_delta)
                curr_belly += curr_treasure_delta
        
        best_treasures = max(best_treasures, len(selected_treasure_deltas))
    
    return best_treasures


def main():
    T = int(input())
    for _ in range(T):
        F, B = map(int, input().split())
        N, M, S, E = map(int, input().split())

        X, Y = [None] * M, [None] * M
        for i in range(M):
            X[i], Y[i] = map(int, input().split())

        U, V = [None] * F, [None] * F
        for i in range(F):
            U[i] = int(input()) 
            V[i] = 1
        
        print(solve(F, B, N, M, S, E, X, Y, U, V))


if __name__ == '__main__':
    main()
