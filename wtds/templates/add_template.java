import java.io.*;

class Solution {
    /*
    * Find the unknown datamon through feed, poop, and guess queries.
        
    * Call the feed, poop, and guess functions below to make feed, poop, and guess queries.
    */
     static void solve() throws IOException {
         // YOUR CODE HERE
     }

    /*
    * Feed the datamon an integer
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
    * Datamon poops out an integer depending on its species 
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
    * Guess the datamon 
    */
     static String guess(String i) throws IOException {
         out.println("guess " + i);
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
         String response = in.readLine();
     }
 }