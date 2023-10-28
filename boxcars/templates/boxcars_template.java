import java.io.*;

class Solution {
    /**
     * Output two lines containing the sides of the dice separated by dashes -,
     * such that the two dice yield the given sum distribution S.
     * 
     * S: a list containing the possible 36 sums achieved rolling the two unknown die.
     */
    static void solve(int[] S) {
        // YOUR CODE HERE
        return;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int[] S = new int[36];
            for (int j = 0; j < 36; ++j) {
                S[j] = parseInt(temp[j]);
            }
            solve(S);
        }
        out.flush();
    }
}