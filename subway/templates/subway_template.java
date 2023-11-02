import java.io.*;

class Solution {
    /**
     * Find the distance the subway must travel before all passengers
     * arrive at their ending station
     * 
     * N: the number of passengers
     * M: the number of stations
     * K: the capacity of the train
     * S: the list of starting stations for each passenger
     * E: the list of ending stations for each passenger
     * P: the list of line positions for each passenger at their station
     */
    static int solve(int N, int M, int K, int[] S, int[] E, int[] P) {
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
            int[] S = new int[N];
            temp = in.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                S[j] = Integer.parseInt(temp[j]);
            }
            int[] E = new int[N];
            temp = in.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                E[j] = Integer.parseInt(temp[j]);
            }
            int[] P = new int[N];
            for (int j = 0; j < N; j++) {
                P[j] = Integer.parseInt(temp[j]);
            }
            solve(N, M, K, S, E, P);
        }
        out.flush();
    }
}