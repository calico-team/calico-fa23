import java.io.*;

class Solution {
    /**
     * Identify the unknown datamon through making feed and poop queries.
     *  
     * Call the feed and poop functions below to make feed and poop queries.
     * Return from this function after calling the guess function to make a
     * guess query.
     */
    static void solve() throws IOException {         
        // YOUR CODE HERE
    }
    
    /*
     * Feed a number to the Datamon. Returns OK if successful.
     */
    static String feed(int i) throws IOException {
        out.println("feed " + i);
        out.flush();
        String response = in.readLine();
        if (response.equals("WRONG_ANSWER")) {
            System.exit(0);
        }
        return response;
    }
    
    /*
     * Get the Datamon to poop out a number. Returns the number pooped out.
     */
    static int poop() throws IOException {
        out.println("poop");
        out.flush();
        String response = in.readLine();
        if (response.equals("WRONG_ANSWER")) {
            System.exit(0);
        }
        return Integer.valueOf(response);
    }
    
    /*
     * Guess the species of the Datamon and end this test case. Returns CORRECT
     * if the guess is correct. Exits otherwise.
     */
    static String guess(String s) throws IOException {
        out.println("guess " + s);
        out.flush();
        String response = in.readLine();
        if (response.equals("WRONG_ANSWER")) {
            System.exit(0);
        }
        return response;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            solve();
        }
        out.flush();
    }
}
 