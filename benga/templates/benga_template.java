import java.io.*;

class Solution {
    /**
    * Return the number of possible towers that Big Ben can build with N blocks.
    * 
    * @param N : number of 1x1x3 Benga Bricks we can use to construct the Benga tower.
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
