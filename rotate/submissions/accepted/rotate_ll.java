import java.io.*;

class Solution {
    static class LinkedListNode {
        int val;
        LinkedListNode next;
        
        LinkedListNode(int val) {
            this.val = val;
            this.next = null;
        }
    }
    
    static int solve(int N, int K) {
        LinkedListNode sentinel = new LinkedListNode(-1);
        LinkedListNode curr = sentinel, top = sentinel;
        for (int i = 1; i <= N; i++) {
            top.next = new LinkedListNode(i);
            top = top.next;
        }
        
        for (int i = 0; i < N; i++) {
            top.next = curr.next;
            curr.next = curr.next.next;
            top = top.next;
            curr = curr.next;
        }
        
        for (int i = 1; i <= N; i++) {
            sentinel = sentinel.next;
            if (sentinel.val == K) {
                return i;
            }
        }
        
        return -1;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] line = in.readLine().split(" ");
            int N = Integer.parseInt(line[0]);
            int K = Integer.parseInt(line[1]);
            out.println(solve(N, K));
        }
        out.flush();
    }
}
