import java.io.*;

class Solution {
    /**
     * Find the total distance the subway must travel until all passengers have
     * arrived at their ending station.
     * 
     * N: the number of passengers
     * M: the number of stations
     * K: the maximum number of passengers the subway can carry
     * S: list of starting stations for each passenger
     * E: list of ending stations for each passenger
     */
    static int solve(int N, int M, int K, int[] S, int[] E) {
        // YOUR CODE HERE
        return -1;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int N = Integer.parseInt(temp[0]);
            int M = Integer.parseInt(temp[1]);
            int K = Integer.parseInt(temp[2]);
            temp = in.readLine().split(" ");
            int[] S = new int[N];
            for (int j = 0; j < N; j++) {
                S[j] = Integer.parseInt(temp[j]);
            }
            temp = in.readLine().split(" ");
            int[] E = new int[N];
            for (int j = 0; j < N; j++) {
                E[j] = Integer.parseInt(temp[j]);
            }
            out.println(solve(N, M, K, S, E));
        }
        out.flush();
    }
}
