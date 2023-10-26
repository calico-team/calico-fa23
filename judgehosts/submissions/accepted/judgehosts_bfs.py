from collections import deque

def solve(N, M, S, U, V):
    # Solution is an articulation point which is neither a contestant nor judgehost.
    adj = [[] for _ in range(N + 1)]
    contestants = [True] * (N + 1)
    judgehosts = [True] * (N + 1)
    for i in range(M):
        adj[U[i]].append(V[i])
        contestants[V[i]] = False
        judgehosts[U[i]] = False

    visited = [False] * (N + 1)
    q = deque()
    for i in range(1, N + 1):
        if contestants[i]:
            q.append(i)
            visited[i] = True

    while q:
        u = q.popleft()
        if not q and not contestants[u] and not judgehosts[u]:
            print("1")
            print(u)
            return
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    print("IMPOSSIBLE")

def main():
    T = int(input())
    for _ in range(T):
        N, M, S = map(int, input().split())
        U = [0] * M
        V = [0] * M
        for j in range(M):
            U[j], V[j] = map(int, input().split())
        solve(N, M, S, U, V)

if __name__ == "__main__":
    main()