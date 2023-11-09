import java.io.*;

class Solution {
    /**
     * Output a single line containing K - 1 space-separated values denoting
     * the maximum fuel charge possible for each leg of the journey.
     *     
     * N: the number of universes
     * M: the number of portals
     * K: the number of errands
     * U: the list containing the sequence of universes in which errands are to be completed
     * A: the list of A_i for each portal
     * B: the list of B_i for each portal
     * C: the list of fuel charges for each portal
     */
    static void solve(int N, int M, int K, int[] U, int[] A, int[] B, int[] C) {
        // YOUR CODE HERE
        return;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int N = Integer.parseInt(temp[0]), M = Integer.parseInt(temp[1]), K = Integer.parseInt(temp[2]);
            int[] U = new int[K];
            temp = in.readLine().split(" ");
            for (int j = 0; j < K; j++) {
                U[j] = Integer.parseInt(temp[j]);
            }
            int[] A = new int[M], B = new int[M], C = new int[M];
            for (int j = 0; j < K; j++) {
                temp = in.readLine().split(" ");
                A[j] = Integer.parseInt(temp[0]);
                B[j] = Integer.parseInt(temp[1]);
                C[j] = Integer.parseInt(temp[2]);
            }
            solve(N, M, K, U, A, B, C);
        }
        out.flush();
    }
}
