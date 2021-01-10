import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
        HashSet<List<Integer>> ans = new HashSet<>();
        if (nums.length <3){
            return new ArrayList<>(ans);
        }
        Arrays.sort(nums);
        for(int i =0; i <nums.length-1 ; i++){
            if(i>0 && nums[i] == nums[i-1])
                continue;
            int left = 0 - nums[i];
            int l = i+1;
            int r = nums.length-1;
            while ( l < r){
                int sum = nums[l] + nums[r];
                if(sum == left){
                    List<Integer> t = new ArrayList<>();
                    t.add(nums[i]);
                    t.add(nums[l]);
                    t.add(nums[r]);
                    ans.add(t);
                    l++;
                    r--;
                }else if (sum < left){
                    l++;
                }else{
                    r--;
                }
            }
        }
        return new ArrayList<>(ans);
    }
}
