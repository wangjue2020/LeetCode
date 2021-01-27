public class SearchInRotatedSortedArray {
    /**
     * binary search
     * O(logn)
     * @param nums
     * @param target
     * @return
     */
    public int search1(int[] nums, int target) {
        if(target == nums[0])
            return 0;
        if(target == nums[nums.length-1])
            return nums.length-1;
        int l = 0;
        int r = nums.length-1;
        while(l<=r){
            int mid = (l+r) /2;
            if(nums[mid] == target ){
                return mid;
            }else if (target > nums[mid]){
                if(nums[mid]>= nums[l]){
                    l = mid+1;
                }else{
                    if(target >= nums[l]){
                        r = mid-1;
                    }else{
                        l = mid +1;
                    }
                }
            }else{
                if(nums[mid] >= nums[l]){
                    if(target < nums[l]){
                        l = mid+1;
                    }else{
                        r = mid-1;
                    }
                }else{
                    r= mid-1;
                }

            }
        }
        return -1;
    }
    /**
     * 判断从前往后还是从后往前
     * O(n/2) 即 O(N)
     * @param nums
     * @param target
     * @return
     */
    public int search(int[] nums, int target) {
        if(target == nums[0])
            return 0;
        if(target == nums[nums.length-1])
            return nums.length-1;
        if(target > nums[0]){
            for(int i = 1; i< nums.length && nums[i] >= nums[i-1]; i++){
                if(nums[i] == target)
                    return i;
            }
        }else{
            for(int i = nums.length-2; i >=0 && nums[i] <= nums[i+1]; i--){
                if(nums[i] == target)
                    return i;
            }
        }
        return -1;
    }
}
