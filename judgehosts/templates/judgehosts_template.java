package templates;
import java.io.*;

class Solution {
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
        // YOUR CODE HERE
        // Print in the first line the number of computers Bessie the Cow should eat
        // Print in the next line each of the computers she should eat
        // If it's impossible for Bessie the Cow to ruin the contest, print "IMPOSSIBLE"
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
