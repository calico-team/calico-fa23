import java.io.*;
import java.util.*;

class Solution {
    static int solve(int N, int K) {
        List<Integer> deck = new ArrayList<>();
        for (int i = 1; i <= N; i++) {
            deck.add(i);
        }
        
        for (int i = 0; i < N; i++) {
            int card = deck.remove(i);
            deck.add(card);
        }
        
        return deck.indexOf(K) + 1;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] line = in.readLine().split(" ");
            int N = Integer.parseInt(line[0]);
            int K = Integer.parseInt(line[1]);
            out.println(solve(N, K));
        }
        out.flush();
    }
}
