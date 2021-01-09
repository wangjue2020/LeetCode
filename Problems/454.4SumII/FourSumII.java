import java.util.HashMap;

public class FourSumII {
    public int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
        HashMap<Integer, Integer> p1 = possibleSumOfTwoArr(A,B);
        HashMap<Integer, Integer> p2 = possibleSumOfTwoArr(C,D);

        int ans = 0;
        for (int sum : p1.keySet()){
            int val = p2.getOrDefault(-sum, 0);
            int res = p1.get(sum) * val;
            ans += res;
        }
        return ans;
    }

    public HashMap<Integer, Integer> possibleSumOfTwoArr(int[] A, int[] B){
        HashMap<Integer, Integer> ans = new HashMap<>();
        for(int i: A){
            for(int j: B){
                int sum = i+j;
                int val = ans.getOrDefault(sum, 0);
                ans.put(sum, ++val);
            }
        }
        return ans;
    }
}
