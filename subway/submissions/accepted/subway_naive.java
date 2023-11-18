import java.io.*;
import java.util.*;

class Solution {
    static int solve(int N, int M, int K, int[] S, int[] E) {
        List<List<Integer>> stations = new ArrayList<>();
        for (int i = 0; i <= M; i++) {
            stations.add(new ArrayList<>());
        }
        for (int i = 0; i < N; i++) {
            stations.get(S[i]).add(E[i]);
        }
        
        int passengersDone = 0, totalDist = 0, currStation = 1;
        List<Integer> train = new ArrayList<>();
        while (true) {
            while (train.contains(currStation)) {
                train.remove(Integer.valueOf(currStation));
                passengersDone++;
            }
            
            while (stations.get(currStation).size() > 0 && train.size() < K) {
                train.add(stations.get(currStation).remove(0));
            }
            
            if (passengersDone < N) {
                currStation = currStation % M + 1;
                totalDist++;
            } else {
                break;
            }
        }
        
        return totalDist;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int N = Integer.parseInt(temp[0]);
            int M = Integer.parseInt(temp[1]);
            int K = Integer.parseInt(temp[2]);
            temp = in.readLine().split(" ");
            int[] S = new int[N];
            for (int j = 0; j < N; j++) {
                S[j] = Integer.parseInt(temp[j]);
            }
            temp = in.readLine().split(" ");
            int[] E = new int[N];
            for (int j = 0; j < N; j++) {
                E[j] = Integer.parseInt(temp[j]);
            }
            out.println(solve(N, M, K, S, E));
        }
        out.flush();
    }
}
