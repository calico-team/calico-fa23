import java.io.*;

class Solution {
     static void solve() throws IOException {         
        feed(2);
        feed(1);
        feed(3);
        
        int num = poop();
        if (num == 2) {
            guess("queueon");
        } else if (num == 1) {
            guess("heapeon");
        } else {
            guess("stackeon");
        }
     }

     static String feed(int i) throws IOException {
         out.println("feed " + i);
         out.flush();
         String response = in.readLine();
         if (response.equals("WRONG_ANSWER")) {
             System.exit(0);
         }
         return response;
     }

     static int poop() throws IOException {
         out.println("poop");
         out.flush();
         String response = in.readLine();
         if (response.equals("WRONG_ANSWER")) {
             System.exit(0);
         }
         return Integer.valueOf(response);
     }

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
 