import java.util.Arrays;

public class MajorityElement {
    /**
     * Boyer-Moore Voting Algorithm
     * @param nums
     * @return
     */
    public int majorityElementVote(int[] nums) {
        int count = 1;
        int majority = nums[0];
        for(int i = 1; i < nums.length; i++){
            if(count==0)
                majority=nums[i];
            if(nums[i] == majority)
                count++;
            else
                count--;
        }
        return majority;
    }
    /**
     * Using sort
     * @param nums
     * @return
     */
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length/2];
    }
}
