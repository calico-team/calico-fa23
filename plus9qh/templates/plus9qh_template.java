import java.io.*;

class Solution {
    /**
    Output a program that outputs the given text.

    T: the number of Test Cases
    N: the number of lines in the program
    X: the list of lines of the program
     */
    static void solve(int N, int[] X) {
        // YOUR CODE HERE
        return;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] info = in.readLine().split(" ");
            int N = Integer.parseInt(info[0]);
            int[] X = new int[N];
            for (int j = 0; j < N; j++) {
                String[] trail = in.readLine().split(" ");
                X[j] = Integer.parseInt(trail[0]);
            }
            solve(N, X);
        }
        out.flush();
    }
}
