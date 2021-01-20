public class HouseRobber {
    public int rob(int[] nums) {
        int ans = 0;
        if(nums.length == 0)
            return ans;
        if(nums.length == 1){
            return nums[0];
        }
        ans = nums[0];
        for(int i= 1; i < nums.length; i++){
            int p2 = (i-2>=0)? nums[i-2]: 0;
            int p3 = (i-3>=0)? nums[i-3]:0;
            nums[i] = nums[i] + ((p2>p3) ?p2 : p3);
            ans = (ans > nums[i]) ? ans:nums[i];
        }
        return ans;
    }
}
