import java.io.*;

class Solution {
    /**
     * Given the layout of a mystery dungeon, find the largest
     * value of treasure you can collect before running out of belly.
     * 
     * F: the number of floors in the mystery dungeon
     * B: your belly capacity
     * N: the number of nodes on each floor the of the mystery dungeon
     * M: the number of edges on each floor of the mystery dungeon
     * S: the node where the spawn point is located
     * E: the node where the exit stairwell is located
     * X: the list of X_i for each undirected edge
     * Y: the list of Y_i for each undirected edge
     * U: the node where the treasure on floor i is located
     * V: the value of the treasure on floor i
     */
    static void solve(int F, int B, int N, int M, int S, int E, int[] X, int[] Y, int[] U, int[] V) {
        // YOUR CODE HERE
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] info = in.readLine().strip().split(" ");
            int F = Integer.parseInt(info[0]);
            int B = Integer.parseInt(info[1]);

            info = in.readLine().strip().split(" ");
            int N = Integer.parseInt(info[0]);
            int M = Integer.parseInt(info[1]);
            int S = Integer.parseInt(info[2]);
            int E = Integer.parseInt(info[3]);

            int[] X = new int[M];
            int[] Y = new int[M];
            int[] U = new int[F];
            int[] V = new int[F];

            for (int j = 0; j < M; j++) {
                info = in.readLine().strip().split(" ");
                X[j] = Integer.parseInt(info[0]);
                Y[j] = Integer.parseInt(info[1]);
            }

            for (int j = 0; j < F; j++) {
                info = in.readLine().strip().split(" ");
                U[j] = Integer.parseInt(info[0]);
                V[j] = Integer.parseInt(info[1]);
            }

            solve(F, B, N, M, S, E, X, Y, U, V);
        }
        out.flush();
    }
}