import java.io.*;
import java.math.BigInteger;

class Solution {
    /**
     * Implements addition with Java's BigInteger class and string parsing.
     */
    static String solve(String A, String B) {
        return new BigInteger(A).add(new BigInteger(B)).toString();
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
