def solve(N: int, M: int, Q: int, U: list[int], V: list[int], A: list[int], B: list[int], C: list[int]):
    nodes_xor = [0 for _ in range(N + 1)]
    graph = {}
    for i in range(M):
        graph[A[i]].append({B[i], C[i]})
        graph[B[i]].append({A[i], C[i]})

    dfs_tree = {}
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
                dfs_tree[u].append({v, w})
                dfs(v)

    def triangles(u, p):
        for v, w in dfs_tree[u]:
            triangles(v, u)
        for v, w in graph[u]:
            if v != p:
                add_to_basis(w ^ nodes_xor[u] ^ nodes_xor[v])

    dfs(1)
    triangles(1, 0)

    for i in range(Q):
        answer = nodes_xor[U[i]] ^ nodes_xor[V[i]]
        for b in basis:
            answer = max(answer, answer ^ b)
        print(answer)


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        N, M, Q = int(temp[0]), int(temp[1]), int(temp[2])
        U = [None for _ in range(Q)]
        V = [None for _ in range(Q)]
        A = [None for _ in range(M)]
        B = [None for _ in range(M)]
        C = [None for _ in range(M)]
        for i in range(M):
            temp = input().split()
            A[i], B[i], C[i] = int(temp[0]), int(temp[1]), int(temp[2])
        for i in range(Q):
            temp = input().split()
            U[i], V[i] = int(temp[0]), int(temp[1])

        solve(N, M, Q, U, V, A, B, C)


if __name__ == '__main__':
    main()
