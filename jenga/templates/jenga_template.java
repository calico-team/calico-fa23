import java.io.*;

class Solution {
    /**
    * Return the number of unique Jenga towers that can be built using N or
    * fewer bricks. Give your answer modulo 3359232.
    * 
    * N: the maximum number of bricks to use
    */
    static int solve(long N) {
        // YOUR CODE HERE
        return -1;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            long N = Long.parseLong(temp[0]);
            out.println(solve(N));
        }
        out.flush();
    }
}