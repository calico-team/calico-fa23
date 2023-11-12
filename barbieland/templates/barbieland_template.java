import java.io.*;

class Solution {
    /**
     * Output Q lines, where the i-th line contains the maximum
     * fuel charge possible for the i-th errand
     *
     * N: the number of universes
     * M: the number of portals
     * Q: the number of queries
     * U: the list containing U_i for each query
     * V: the list containing V_i for each query
     * A: the list of A_i for each portal
     * B: the list of B_i for each portal
     * C: the list of fuel charges for each portal
     *
     */
    static void solve(int N, int M, int Q, int[] U, int[] V, int[] A, int[] B, int[] C) {
        // YOUR CODE HERE
        return;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int N = Integer.parseInt(temp[0]), M = Integer.parseInt(temp[1]), Q = Integer.parseInt(temp[2]);
            int[] U = new int[K], V = new int[K];
            int[] A = new int[M], B = new int[M], C = new int[M];
            for (int j = 0; j < K; j++) {
                temp = in.readLine().split(" ");
                A[j] = Integer.parseInt(temp[0]);
                B[j] = Integer.parseInt(temp[1]);
                C[j] = Integer.parseInt(temp[2]);
            }
            for (int j = 0; j < K; ++j) {
                temp = in.readLine().split(" ");
                U[j] = Integer.parseInt(temp[0]);
                V[j] = Integer.parseInt(temp[1]);
            }
            solve(N, M, Q, U, V, A, B, C);
        }
        out.flush();
    }
}
