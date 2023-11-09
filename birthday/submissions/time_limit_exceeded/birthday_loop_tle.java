import java.io.*;

class Solution {
    static long solve(long N) {
        long numDays = 0;
        for (int i = 1; i < N; i++){
            numDays += (long)i * (long)i;
        }
        return numDays + 3;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            long N = Long.parseLong(in.readLine());
            out.println(solve(N));
        }
        out.flush();
    }
}
