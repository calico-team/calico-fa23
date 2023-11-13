import java.io.*;

class Solution {
    /**
     * Output Q lines, where the i-th line contains the maximum
     * fuel charge possible for the i-th errand
     *     
     * N: the number of universes
     * M: the number of portals
     * Q: the number of queries
     * U: the list of U_i for each portal
     * V: the list of V_i for each portal
     * W: the list of W_i for each portal
     * A: the list of A_i for each errand
     * B: the list of B_i for each errand
     * 
     */
    static void solve(int N, int M, int Q, int[] U, int[] V, long[] W, int[] A, int[] B) {
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
            int[] U = new int[M], V = new int[M], A = new int[Q], B = new  int[Q];
            long[] W = new long[M];
            for (int j = 0; j < K; j++) {
                temp = in.readLine().split(" ");
                U[j] = Integer.parseInt(temp[0]);
                V[j] = Integer.parseInt(temp[1]);
                W[j] = Long.parseLong(temp[2]);
            }
            for (int j = 0; j < K; ++j) {
                temp = in.readLine().split(" ");
                A[j] = Integer.parseInt(temp[0]);
                B[j] = Integer.parseInt(temp[1]);
            }
            solve(N, M, Q, U, V, W, A, B);
        }
        out.flush();
    }
}
