import java.io.*;

class Solution {
    /**
     * Return the number of days between Year 0 and Big Ben's Birthday
     *
     * N: The number of years before Big Ben's Birthday
     */
    static int solve(int N) {
        // YOUR CODE HERE
        return -1;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseLong(in.readLine());
            out.println(solve(N));
        }
        out.flush();
    }
}
