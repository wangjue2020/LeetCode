import java.util.HashMap;
import java.util.Map;

public class ContainsDuplicateII {
    /**
     * Use HashMap
     * @param nums
     * @param k
     * @return
     */
    public boolean containsNearbyDuplicateMap(int[] nums, int k) {
        Map<Integer,Integer> map = new HashMap<>();
        for(int i =0; i<nums.length; i++){
            int val = map.getOrDefault(nums[i],-1);
            if(val != -1 && i-val <=k)
                return true;
            else{
                map.put(nums[i],i);
            }
        }
        return false;
    }
    /**
     * Brute Force: nested loop
     * @param nums
     * @param k
     * @return
     */
    @Deprecated
    public boolean containsNearbyDuplicate(int[] nums, int k) {
         for(int i=0; i < nums.length; i++){
             for(int j=1;j <= k && i+j < nums.length; j++){
                 if(nums[i] == nums[i+j])
                     return true;
             }
         }
         return false;
    }
}
