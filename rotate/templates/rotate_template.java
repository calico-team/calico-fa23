import java.io.*;

class Solution {
    /**
     * Return the position of the card labelled K after shuffling a deck with N cards.
     * 
     * N: a non-negative integer
     * K: another non-negative integer
     */
    static int solve(int N, int K) {
        // YOUR CODE HERE
        return 0;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] line = in.readLine().split(" ");
            int N = Integer.parseInt(line[0]);
            int K = Integer.parseInt(line[1]);
            out.println(solve(N,K));
        }
        out.flush();
    }
}
