import java.io.*;

class Solution {
    /**
     * Return the berkeleytime value of A.
     * 
     * A: a non-negative integer
     */
    static String solve(int A) {
        String solutionString;

        if (A > 180) {
            return "canceled";
        }
        for (int i = 0; i < A % 10; i++) {
            solutionString += "berkeley";
        }

        return solutionString + "time";
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
