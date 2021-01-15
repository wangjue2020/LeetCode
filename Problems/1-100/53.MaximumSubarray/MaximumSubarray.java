public class MaximumSubarray {
    public int maxSubArray(int[] nums) {
        int ans =nums[0];
        for(int i = 1; i < nums.length; i++){
            nums[i] = Integer.max(nums[i], nums[i]+nums[i-1]);
            ans = nums[i] >= ans? nums[i]: ans;
        }
        return ans;
    }
}
