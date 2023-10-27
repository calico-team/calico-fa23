import java.io.*;

class Solution {
    /**
     * Find an HQ9+ program that outputs exactly the given text or return
     * IMPOSSIBLE if no solutions exist.
     * 
     * N: the number of lines of text
     * X: a list containing the lines of the text
     */
    static String solve(int N, String[] X) {
        out.println(N);
        for (String s : X) {
            out.println(X);
        }
        // YOUR CODE HERE
        return "";
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(in.readLine());
            String[] X = new String[N];
            for (int j = 0; j < N; j++) {
                X[j] = in.readLine();
            }
            out.println(solve(N, X));
        }
        out.flush();
    }
}
