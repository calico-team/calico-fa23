import java.io.*;
import java.util.*;

class judgehosts_bfs {
    /**
     * Print in the first line the number K of commputers Bessie the Cow should eat.
     * Print in the next line K numbers, one for each different computer she should eat.
     * If her task is not possible, print "IMPOSSIBLE"
     *
     * @param N Number of computers.
     * @param M Number of connections between computers.
     * @param S Number of stomachs.
     * @param U Initial computer for each of the M connections.
     * @param V Final computer for each of the M connections.
     */
    static void solve(int N, int M, int S, int[] U, int[] V) {
        ArrayList<Integer>[] adj = new ArrayList[N + 1];
        for (int i = 0; i < N + 1; i++) {
            adj[i] = new ArrayList<>();
        }

        boolean[] isContestant = new boolean[N + 1], isJudgehost = new boolean[N + 1];
        Arrays.fill(isContestant, true);
        Arrays.fill(isJudgehost, true);

        for (int i = 0; i < M; i++) {
            adj[U[i]].add(V[i]);
            isContestant[V[i]] = false;
            isJudgehost[U[i]] = false;
        }

        boolean[] vis = new boolean[N + 1];
        ArrayDeque<Integer> q = new ArrayDeque<>();

        for (int i = 1; i <= N; i++) {
            if (isContestant[i]) {
                q.push(i);
                vis[i] = true;
            }
        }

        while (!q.isEmpty()) {
            int cur = q.pop();
            if (q.isEmpty() && !isContestant[cur] && !isJudgehost[cur]) {
                out.println("1\n" + cur);
                return;
            }
            for (int to : adj[cur]) {
                if (!vis[to]) {
                    vis[to] = true;
                    q.add(to);
                }
            }
        }

        out.println("IMPOSSIBLE");
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
}
