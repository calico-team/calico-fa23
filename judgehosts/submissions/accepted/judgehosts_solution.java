package solutions;
import java.io.*;
import java.util.*;

class Solution {

    /**
     * Bessie the Cow can only ruin CALICO if there is a point in
     * time where only one computer has submissions that have to be sent, as she
     * only has 1 stomach.
     * We can turn the next computers from a contestant into "fake contestants",
     * since they also have submissions to be judged.
     * 
     * This behaviour is the same as running a multi-source BFS from each contestant,
     * and check if the queue is empty at any point. The idea is the same as a topological sort.
     * 
     * Time complexity: O(N + M)
    */
    static void bfs_solution(int N, int M, int S, int[] U, int[] V) {

        ArrayList<ArrayList<Integer>> adj = new ArrayList<>(N + 1);

        // Add edges to the graph
        for (int i = 0; i < M; ++i) {
            adj.get(U[i]).add(V[i]);
        }

        // Check which computers are judges
        boolean[] is_judge = new boolean[N + 1];
        for (int i = 0; i < N + 1; ++i) {
            is_judge[i] = true;
        }
        for (int i = 0; i < M; ++i) {
            is_judge[U[i]] = false;
        }

        // Add one "super judge" at index 0
        for (int i = 1; i <= N; ++i) {
            if (is_judge[i]) {
                adj.get(i).add(0);
            }
        }

        // Chech which computers are contestants and add them to the BFS queue
        ArrayDeque<Integer> contestants = new ArrayDeque<>();
        boolean[] is_contestant = new boolean[N + 1];
        is_contestant[0] = false;
        for (int i = 0; i < M; ++i) {
            is_contestant[V[i]] = false;
        }
        for (int i = 0; i <= N; ++i) {
            if (is_contestant[i]) {
                contestants.addLast(i);
            }
        }

        // Run algorithm:
        while (!contestants.isEmpty()) {
            int contestant = contestants.getFirst();
            contestants.removeFirst();
            // 0 is an imaginary computer, so we also have to check that it's different from 0
            // Bessie the Cow cannot eat imaginary computers (yet).
            if (contestant != 0 && contestants.isEmpty()) {
                // This is a solution
                out.println(1);
                out.println(contestant);
                return;
            }

            for (int computer : adj.get(contestant)) {
                if (!is_contestant[computer]) {
                    is_contestant[computer] = true;
                    contestants.addLast(computer);
                }
            }
        }

        out.println("IMPOSSIBLE\n");

    }


    /**
     * Description: Calculates maximum flow of a graph
     * Time: $O(N^2M)$ flow, $O(M\sqrt N)$ bipartite matching
     * Source: KACTL, https://github.com/kth-competitive-programming/kactl/blob/main/content/graph/Dinic.h
     * @TODO: Check it works XD
     */

    public static class Dinic {
        static class Edge {
            int to, rev;
            long c, oc;
    
            long flow() {
                return Math.max(oc - c, 0L);
            }

            public Edge(int _to, int _rev, long _c, long _oc) {
                to = _to; rev = _rev; c = _c; oc = _oc;
            }
        }
    
        private List<Integer> lvl, ptr, q;
        private List<List<Edge>> adj;
    
        public Dinic(int n) {
            lvl = new ArrayList<>(n);
            ptr = new ArrayList<>(n);
            q = new ArrayList<>(n);
            adj = new ArrayList<>(n);
    
            for (int i = 0; i < n; i++) {
                lvl.add(0);
                ptr.add(0);
                q.add(0);
                adj.add(new ArrayList<>());
            }
        }
    
        public void addEdge(int a, int b, long c, long rcap) {
            adj.get(a).add(new Edge(b, adj.get(b).size(), c, c)); 
            adj.get(b).add(new Edge(a, adj.get(a).size() - 1, rcap, rcap));
        }
    
        public long dfs(int v, int t, long f) {
            if (v == t || f == 0)
                return f;
            for (int i = ptr.get(v); i < adj.get(v).size(); i++, ptr.set(v, ptr.get(v) + 1)) {
                Edge e = adj.get(v).get(i);
                if (lvl.get(e.to) == lvl.get(v) + 1) {
                    long p = dfs(e.to, t, Math.min(f, e.c));
                    if (p > 0) {
                        e.c -= p;
                        adj.get(e.to).get(e.rev).c += p;
                        return p;
                    }
                }
            }
            return 0;
        }
    
        public long calc(int s, int t) {
            long flow = 0;
            q.set(0, s);
            for (int L = 0; L < 31; ++L) do {
                lvl = new ArrayList<>(q.size());
                ptr = new ArrayList<>(q.size());
                int qi = 0, qe = lvl.set(s, 1);
                while (qi < qe && lvl.get(t) == 0) {
                    int v = q.get(qi++);
                    for (Edge e : adj.get(v)) {
                        if (lvl.get(e.to) == 0 && (e.c >> (30 - L)) > 0) {
                            q.set(qe, e.to);
                            qe++;
                            lvl.set(e.to, lvl.get(v) + 1);
                        }
                    }
                }
                while (true) {
                    long p = dfs(s, t, Long.MAX_VALUE);
                    if (p == 0)
                        break;
                    flow += p;
                }
            } while (lvl.get(t) != 0);
            return flow;
        }
    
        public boolean leftOfMinCut(int a) {
            return lvl.get(a) != 0;
        }
    };

    static int inIdx(int i) { return 2 * i; }
    static int outIdx(int i) { return 2 * i + 1; }

    /**
     * Bessie the Cow will be able to eat enough computers with her S stomachs if
     * we can take out a number S' <= S of nodes in the connectivity graph such that
     * no contestant is able to reach a judge host.
     * 
     * This number S' can be calculated with a flow graph, adding a source node that connects to
     * every contestant, a sink node that will be connected to every judge host and duplicating
     * each computer, adding a flow of 1 in between. The maximum flow of the graph 
     * from the source to the sink is precisely S'.
     * 
     * We can do this using a maxflow algorithm such as Dinic.
     * 
     * Time complexity: O((M + N)√N) (the flow graph is bipartite since we are duplicating the nodes)
    */  
    static void mincut_solution(int N, int M, int S, int[] U, int[] V) {
        Dinic flow = new Dinic(2 * N + 2);
        int source = 0, sink = 1;
        // S + 1 is a good "infinity" in the sense that if the answer is bigger than that, we return false.
        int INF = S + 1;
        // Check which computer are contestants and which are judges.
        boolean[] is_contestant = new boolean[N + 1];
        for (int i = 1; i < N + 1; ++i) is_contestant[i] = true;
        boolean[] is_judge = new boolean[N + 1];
        for (int i = 1; i < N + 1; ++i) is_judge[i] = true;
        for (int i = 0; i < M; ++i) {
            is_contestant[V[i]] = false;
            is_judge[U[i]] = false;
        }
        // Connect source to contestants.
        for (int i = 1; i <= N; ++i) {
            if (is_contestant[i]) {
                flow.addEdge(source, inIdx(i), INF, 0);
            }
        }
        // Connect judges to sink.
        for (int i = 1; i <= N; ++i) {
            if (is_judge[i]) {
                flow.addEdge(outIdx(i), sink, INF, 0);
            }
        }
        // Duplicate nodes
        for (int i = 1; i <= N; ++i) {
            flow.addEdge(inIdx(i), outIdx(i), 1, 0);
        }
        // Add edges
        for (int i = 0; i < M; ++i) {
            flow.addEdge(outIdx(U[i]), inIdx(V[i]), INF, 0);
        }
        // Calculate S'
        int S_ = (int)flow.calc(source, sink);
        // If S' > S, there aren't enough stomachs
        if (S_ > S) {
            out.println("IMPOSSIBLE");
        } else {
            out.println(S_);
            // For each node, check if the input and the output are in different parts of the mincut
            for (int i = 1; i <= N; ++i) {
                if (flow.leftOfMinCut(inIdx(i)) ^ flow.leftOfMinCut(outIdx(i))) {
                    out.print(i);
                    out.print(' ');
                }
            }
            out.println();
        }

    }
    

    /**
     * 
     * @param N Number of computers.
     * @param M Number of connections between computers.
     * @param S Number of stomachs.
     * @param U Initial computer for each of the M connections.
     * @param V Final computer for each of the M connections.
     * 
     * @return  True if Bessie the Cow can eat enough computers with
     *          her S stomachs so that no submission is judged. False otherwise.
    */
    static void solve(int N, int M, int S, int[] U, int[] V) {
        if (S == 1) {
            bfs_solution(N, M, S, U, V);
        } else {
            mincut_solution(N, M, S, U, V);
        }
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] info = in.readLine().split(" ");
            int N = Integer.parseInt(info[0]);
            int M = Integer.parseInt(info[1]);
            int S = Integer.parseInt(info[2]);
            int[] U = new int[M];
            int[] V = new int[M];
            for (int j = 0; j < M; j++) {
                String[] connection = in.readLine().split(" ");
                U[j] = Integer.parseInt(connection[0]);
                V[j] = Integer.parseInt(connection[1]);
            }
            solve(N, M, S, U, V);
        }
        out.flush();
    }
};
