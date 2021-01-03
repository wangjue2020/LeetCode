import java.util.*;
public class MinimumSizeSubarraySum {
    public int MinimumSizeSubarraySum(int s, int[] nums) {
        int l = 0;
        int r = 0;
        int ans = 0;
        if(nums.length == 0)
            return ans;
        int sum = nums[r];
        while (r <nums.length && l < nums.length){
            if(sum < s){
                r++;
                if(r < nums.length)
                    sum+= nums[r];
            }else {
                ans = ans == 0? (r-l+1) : Math.min(r-l+1, ans);
                sum -= nums[l];
                l++;
            }
        }
        return ans;
    }
}
