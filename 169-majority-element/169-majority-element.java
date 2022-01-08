class Solution {
    public int majorityElement(int[] nums) {
        return majorityElement(nums, 0, nums.length-1);
    }
    public int count(int[] nums, int s, int e, int num){
        int ans = 0;
        for (int i = s; i <= e; i++){
            if (nums[i] == num)
                ans++;
        }
        return ans;
    }
    public int majorityElement(int[] nums, int s, int e){
        if (s == e) 
            return nums[s];
        else{
            int mid = (s+e) / 2;
            
            int left = majorityElement(nums,s,mid);
            int right = majorityElement(nums, mid+1, e);
            if (left == right) 
                return left;
            else{
                int count_left = count(nums,s,e,left);
                int count_right = count(nums,s,e,right);
                return count_left > count_right ? left : right;
            }
        }
    }
    
}