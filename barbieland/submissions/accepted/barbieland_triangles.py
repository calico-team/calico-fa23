import sys

sys.setrecursionlimit(10 ** 9)


def solve(N: int, M: int, Q: int, U: list[int], V: list[int], W: list[int], A: list[int], B: list[int]):
    nodes_xor = [0 for _ in range(N + 1)]
    graph = [[] for i in range(N + 1)]
    for i in range(M):
        graph[U[i]].append((V[i], W[i]))
        graph[V[i]].append((U[i], W[i]))

    dfs_tree = [[] for i in range(N + 1)]
    visited = set()
    basis = []

    def add_to_basis(x):
        for y in basis:
            x = min(x, y ^ x)
        if x != 0:
            basis.append(x)

    def dfs(u):
        visited.add(u)
        for v, w in graph[u]:
            if v not in visited:
                nodes_xor[v] = nodes_xor[u] ^ w
                dfs_tree[u].append(v)
                dfs(v)

    def triangles(u):
        for v in dfs_tree[u]:
            triangles(v)
        for v, w in graph[u]:
            add_to_basis(w ^ nodes_xor[u] ^ nodes_xor[v])

    dfs(1)
    triangles(1)

    for i in range(Q):
        answer = nodes_xor[A[i]] ^ nodes_xor[B[i]]
        for b in basis:
            answer = max(answer, answer ^ b)
        print(answer)


def main():
    T = int(input())
    for _ in range(T):
        N, M, Q = [int(i) for i in input().split()]
        U, V, W = map(list, zip(*(map(int, input().split()) for _ in range(M))))
        A, B = map(list, zip(*(map(int, input().split()) for _ in range(Q))))
        solve(N, M, Q, U, V, W, A, B)


if __name__ == '__main__':
    main()
