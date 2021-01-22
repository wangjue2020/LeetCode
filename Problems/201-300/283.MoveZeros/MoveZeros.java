public class MoveZeros {
    public void moveZeroes(int[] nums) {
        int ind = 0;
        for(int i = 0; i<nums.length; i++){
            if(nums[i] == 0)
                continue;
            else{
                int temp = nums[i];
                nums[i] =0;
                nums[ind++] = temp;
            }
        }

    }
}
