import java.io.*;

class Solution {
    /**
     * Return the last 9 digits of the number of ways that Big Ben can build his Benga Bricks tower.
     * 
     * @param N : height of the Benga Bricks tower (positive).
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
            long N = Long.parseLong(temp[0]); // CAUTION! For the last Bonus you might want to change this.
            out.println(solve(N));
        }
        out.flush();
    }
}
