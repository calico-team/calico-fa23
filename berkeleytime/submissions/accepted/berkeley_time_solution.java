import java.io.*;

class Solution {
    static String solve(int N) {
        if (N == 0) {
            return "haha good one";
        } else if (N >= 180) {
            return "canceled";
        } else {
            String berkeleys = "";
            for (int i = 0; i < N; i += 10) {
                berkeleys += "berkeley";
            }
            return berkeleys + "time";
        }
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(in.readLine());
            out.println(solve(N));
        }
        out.flush();
    }
}
