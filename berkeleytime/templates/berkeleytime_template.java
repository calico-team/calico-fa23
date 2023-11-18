import java.io.*;

class Solution {
    /**
     * Return the appropriate text given the contest will start N minutes late.
     * 
     * N: the number of minutes late the contest will start
     */
    static String solve(int N) {
        // YOUR CODE HERE
        return "";
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(in.readLine());
            out.println(solve(N));
        }
        out.flush();
    }
}
