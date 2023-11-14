from collections import deque
import sys

class Dinic:
    class Edge:
        def __init__(self, to, rev, c, oc):
            self.to = to
            self.rev = rev
            self.c = c
            self.oc = oc

        def flow(self):
            return max(self.oc - self.c, 0)

    def __init__(self, n):
        self.lvl = [0] * n
        self.ptr = [0] * n
        self.q = [0] * n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, a, b, c, rcap=0):
        self.adj[a].append(self.Edge(b, len(self.adj[b]), c, c))
        self.adj[b].append(self.Edge(a, len(self.adj[a]) - 1, rcap, rcap))

    def dfs(self, v, t, f):
        if v == t or f == 0:
            return f
        while self.ptr[v] < len(self.adj[v]):
            if self.lvl[self.adj[v][self.ptr[v]].to] == self.lvl[v] + 1:
                p = self.dfs(self.adj[v][self.ptr[v]].to, t, min(f, self.adj[v][self.ptr[v]].c))
                if p != 0:
                    self.adj[v][self.ptr[v]].c -= p
                    self.adj[self.adj[v][self.ptr[v]].to][self.adj[v][self.ptr[v]].rev].c += p
                    return p
            self.ptr[v] += 1
        return 0

    def calc(self, s, t):
        flow = 0
        self.q[0] = s
        for L in range(30, 31):
            while True:
                self.lvl = [0] * len(self.q)
                self.ptr = [0] * len(self.q)
                qi = 0
                qe = self.lvl[s] = 1
                while qi < qe and not self.lvl[t]:
                    v = self.q[qi]
                    for e in self.adj[v]:
                        if not self.lvl[e.to] and e.c >> (30 - L) != 0:
                            self.q[qe] = e.to
                            qe += 1
                            self.lvl[e.to] = self.lvl[v] + 1
                    qi += 1
                while True:
                    p = self.dfs(s, t, (1 << 63) - 1)
                    flow += p
                    if p == 0:
                        break
                if self.lvl[t] == 0:
                    break
        return flow

    def left_of_min_cut(self, a):
        return self.lvl[a] != 0

def solve(N, M, S, U, V):
    # Calculate the minimum vertex cut of the graph using Max Flow (Dinic).
    flow = Dinic(2 * N + 2)
    source = 0
    sink = 1

    def in_vertex(i):
        return 2 * i

    def out_vertex(i):
        return 2 * i + 1

    inf = S + 1
    contestants = [True] * (N + 1)
    judgehosts = [True] * (N + 1)

    for i in range(M):
        contestants[V[i]] = False
        judgehosts[U[i]] = False
        flow.add_edge(out_vertex(U[i]), in_vertex(V[i]), inf)

    for i in range(1, N + 1):
        if contestants[i]:
            flow.add_edge(source, in_vertex(i), inf)
            flow.add_edge(in_vertex(i), out_vertex(i), inf)
        elif judgehosts[i]:
            flow.add_edge(out_vertex(i), sink, inf)
            flow.add_edge(in_vertex(i), out_vertex(i), inf)
        else:
            flow.add_edge(in_vertex(i), out_vertex(i), 1)

    computers_needed = flow.calc(source, sink)

    if computers_needed > S:
        print("IMPOSSIBLE")
    else:
        computers_eaten = [i for i in range(1, N + 1) if flow.left_of_min_cut(in_vertex(i)) ^ flow.left_of_min_cut(out_vertex(i))]
        print(*computers_eaten)

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