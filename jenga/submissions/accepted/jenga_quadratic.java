import java.io.*;

class Solution {
    
    static long powmod(long base, long exponent, long modulo) {
        long ans = 1;
        for (long i = 0; i < exponent; ++i) {
            ans = ans * base % modulo;
        }
        return ans;
    }

    static int solve(long N) {
        long ans = 0;
        for (long i = 1; i <= N / 3; ++i) {
            ans += powmod(2, i, 3359232);
            ans %= 3359232;
        }
        return ans;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            long N = Long.parseLong(temp[0]);
            out.println(solve(N));
        }
        out.flush();
    }
}