import java.io.*;

class Solution {
    
    static long binpowmod(long base, long exponent, long modulo) {

        long ans = 1;

        while (exponent != 0) {
            if (exponent % 2 == 1) ans = ans * base % modulo;
            base = base * base % modulo;
            exponent /= 2;
        }

        return ans;

    }

    static long solve(long N) {
        return (binpowmod(2, 1 + N / 3, 3359232) + 3359232 - 2) % 3359232;
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