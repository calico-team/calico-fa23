import java.io.*;

class Solution {
    static String[] LYRICS = new String[] {
        "99 bottles of beer on the wall, 99 bottles of beer.",
        "Take one down and pass it around, 98 bottles of beer on the wall.",
        "98 bottles of beer on the wall, 98 bottles of beer.",
        "Take one down and pass it around, 97 bottles of beer on the wall.",
        "97 bottles of beer on the wall, 97 bottles of beer.",
        "Take one down and pass it around, 96 bottles of beer on the wall."
    };
    static String HELLO = "Hello, world!";

    static String solve(int N, String[] X) {
        String sourceCode = "", soFar = "";

        for (int i = 0; i < N; i++) {
            if (X[i].equals(HELLO)) {
                soFar += "H";
            } else if (X[i].equals(LYRICS[0])) {
                for (int j = 1; j <= 5; j++) {
                    i++;
                    if (i >= N || !X[i].equals(LYRICS[j])) {
                        return "IMPOSSIBLE";
                    }
                }
                soFar += "9";
            } else {
                if (!sourceCode.equals("") && !sourceCode.equals(X[i])) {
                    return "IMPOSSIBLE";
                }
                sourceCode = X[i];
                soFar += "Q";
            }
        }

        if (sourceCode.equals("")) {
            sourceCode = soFar;
        }
        if (sourceCode.replaceAll("\\+", "").equals(soFar)) {
            return sourceCode;
        }
        return "IMPOSSIBLE";
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(in.readLine());
            String[] X = new String[N];
            for (int j = 0; j < N; j++) {
                X[j] = in.readLine();
            }
            out.println(solve(N, X));
        }
        out.flush();
    }
}
