import java.io.*;

class Solution {
    /**
     * TODO: 
     * 
     * A: a non-negative integer
     */
    static int solve(int A) {
        // YOUR CODE HERE
        return -1;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int A = Integer.parseInt(temp[0]);
            out.println(solve(A));
        }
        out.flush();
    }
}
