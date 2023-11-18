import java.io.*;

class Solution {
    /**
     * Output any list of x <= S computers Bessie can eat such that the network is not bridged afterwards.
     * If it's impossible, output IMPOSSIBLE
     * 
     * N: Number of computers.
     * M: Number of connections between computers.
     * S: Number of computers Bessie can eat.
     * U: Initial computer for each of the M connections.
     * V: Final computer for each of the M connections.
     * 
    */
    static void solve(int N, int M, int S, int[] U, int[] V) {
        // YOUR CODE HERE
        return;
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
