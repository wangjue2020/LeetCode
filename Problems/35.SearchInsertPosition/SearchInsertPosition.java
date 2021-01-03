public class SearchInsertPosition {
    /**
     * 二分法
     * @param nums
     * @param target
     * @return
     */
    public int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.length-1;
        while(left <= right){
            int mid = (right+left)/2;
            if(nums[mid] == target){
                return mid;
            }else if( nums[mid] > target){
                right = mid-1;
            } else{
                left = mid+1;
            }
        }
        return left;
    }

    /**
     * 暴力解法
     * @param nums
     * @param target
     * @return
     */
    public int searchInsert1(int[] nums, int target) {
        int ans =0;
        for (int i=0; i < nums.length; i ++){
            if (target <= nums[i]){
                return i;
            }
        }
        return nums.length;

    }
}
