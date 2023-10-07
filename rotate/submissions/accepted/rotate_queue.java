import java.io.*;
import java.util.*;

class Solution {
    static int solve(int N, int K) {
        List<Integer> shuffled = new ArrayList<>();
        Deque<Integer> unshuffled = new ArrayDeque<>();
        for (int i = 1; i <= N; i++) {
            unshuffled.add(i);
        }
        
        while (!unshuffled.isEmpty()) {
            unshuffled.addLast(unshuffled.removeFirst());
            shuffled.add(unshuffled.removeFirst());
        }
        
        return shuffled.indexOf(K) + 1;
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
