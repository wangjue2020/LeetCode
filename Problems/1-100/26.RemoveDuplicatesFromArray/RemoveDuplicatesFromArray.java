public class RemoveDuplicatesFromArray {
    public int removeDuplicates(int[] nums) {
        int ind = 0;
        int cur = 0;
        for(int i =0; i<nums.length; i++){
            if(i == 0){
                ind++;
                cur = nums[i];
                continue;
            }
            if(nums[i] == cur){
                continue;
            }else{
                nums[ind] = nums[i];
                ind++;
                cur = nums[i];
            }
        }
        return ind;
    }
}
