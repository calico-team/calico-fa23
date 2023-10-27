import java.io.*;

class Solution {
    /**
     * Return the sum of A and B.
     * 
     * A: a non-negative integer
     * B: another non-negative integer
     */
    static int solve(int A, int B) {
        // YOUR CODE HERE
        return -1;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int A = Integer.parseInt(temp[0]), B = Integer.parseInt(temp[1]);
            out.println(solve(A, B));
        }
        out.flush();
    }
}
