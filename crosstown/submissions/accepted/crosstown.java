import java.io.*;

class Solution {
    static int solve(int N, int M, int[] S, int[] E) {
        int longest = 0;
        for (int i = 0; i < N; i++) {
            longest = Math.max(longest, (E[i] - S[i] + M) % M);
        }
        return longest;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int N = Integer.parseInt(temp[0]);
            int M = Integer.parseInt(temp[1]);
            temp = in.readLine().split(" ");
            int[] S = new int[N];
            for (int j = 0; j < N; j++) {
                S[j] = Integer.parseInt(temp[j]);
            }
            temp = in.readLine().split(" ");
            int[] E = new int[N];
            for (int j = 0; j < N; j++) {
                E[j] = Integer.parseInt(temp[j]);
            }
            out.println(solve(N, M, S, E));
        }
        out.flush();
    }
}
