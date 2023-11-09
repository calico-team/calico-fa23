import java.io.*;

class Solution {
    /**
     * Output two lines containing the faces of the dice separated by spaces,
     * such that the sorted list of their pairwise sums is equal to S.
     * 
     * S: the list containing the desired nondecreasing list of 36 pairwise sums
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
                S[j] = Integer.parseInt(temp[j]);
            }
            solve(S);
        }
        out.flush();
    }
}