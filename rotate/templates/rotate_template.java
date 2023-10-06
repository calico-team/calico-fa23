import java.io.*;

class Solution {
    /**
     * Return the position of the card labelled K after shuffling a deck with N
     * cards.
     * 
     * N: the number of cards in the deck
     * K: the label of the target card
     */
    static long solve(long N, long K) {
        // YOUR CODE HERE
        return 0;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] line = in.readLine().split(" ");
            long N = Long.parseLong(line[0]);
            long K = Long.parseLong(line[1]);
            out.println(solve(N, K));
        }
        out.flush();
    }
}
