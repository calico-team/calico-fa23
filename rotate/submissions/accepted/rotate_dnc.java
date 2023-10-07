import java.io.*;

class Solution {
    // We need to use long instead of int because 10^18 >= 2^31
    static long solve(long N, long K) {
        if (K % 2 == 0) {
            return K / 2;
        }
        
        if (N % 2 == 0) {
            return N / 2 + solve(N / 2, K / 2 + 1);
        } else {
            if (K == 1) {
                return N / 2 + 1;
            }
            return N / 2 + 1 + solve(N / 2, K / 2);
        }
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
