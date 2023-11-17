import java.io.*;

class Solution {
    /**
     * Given the layout of a mystery dungeon, find the largest
     * number of treasures you can collect before running out of belly.
     * F: the number of floors in the mystery dungeon
     * B: your belly value
     * N: the number of nodes on each floor the of the mystery dungeon
     * M: the number of edges on each floor of the mystery dungeon
     * S: the node where the starting room of each floor is located
     * E: the node where the exit room of each floor is located
     * R: the list of room indices where each treasure room is located
     * U: the list of Ui for each hallway
     * V: the list of Vi for each hallway
     */
    static int solve(int F, int B, int N, int M, int S, int E, int[] R, int[] U, int[] V) {
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

            int[] R = new int[F];
            int[] U = new int[M];
            int[] V = new int[M];

            info = in.readLine().strip().split(" ");
            for (int j = 0; j < F; j++) {
                R[j] = Integer.parseInt(info[j]);
            }
            for (int j = 0; j < M; j++) {
                info = in.readLine().strip().split(" ");
                U[j] = Integer.parseInt(info[0]);
                V[j] = Integer.parseInt(info[1]);
            }

            out.println(solve(F, B, N, M, S, E, R, U, V));
        }
        out.flush();
    }
}