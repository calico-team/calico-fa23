import java.io.*;

class plus9qh {
    static String[] beer = new String[] {"99 bottles of beer on the wall, 99 bottles of beer.",
            "Take one down and pass it around, 98 bottles of beer on the wall.",
            "98 bottles of beer on the wall, 98 bottles of beer.",
            "Take one down and pass it around, 97 bottles of beer on the wall.",
            "97 bottles of beer on the wall, 97 bottles of beer.",
            "Take one down and pass it around, 96 bottles of beer on the wall."};
    static String hello = "Hello, world!";

    /**
     * Find an HQ9+ program that outputs exactly the given text or return
     * IMPOSSIBLE if no solutions exist.
     *
     * N: the number of lines of text
     * X: a list containing the lines of the text
     */
    static String solve(int N, String[] X) {
        String sourceCode = "", soFar = "";

        for (int i = 0; i < N; i++) {
            if (X[i].equals(hello)) {
                soFar += "H";
            } else if (X[i].equals(beer[0])) {
                for (int j = 1; j <= 5; j++) {
                    i++;
                    if (i >= N || !X[i].equals(beer[j])) {
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
        if (sourceCode.replaceAll("\\+","").equals(soFar)) {
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
