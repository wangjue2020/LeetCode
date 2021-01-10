import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class FourSum {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        HashSet<List<Integer>> ans = new HashSet<>();
        if(nums.length<4)
            return new ArrayList<>(ans);
        Arrays.sort(nums);
        for(int i = 0; i<nums.length-3; i++){
            if(i>0&&nums[i] == nums[i-1])
                continue;
            for(int j = i+1; j<nums.length-2; j++){
                if(j >i+1&&nums[j] == nums[j-1])
                    continue;
                int l = j+1;
                int r = nums.length-1;
                while(l<r){
                    int sum = nums[i]+nums[j]+nums[l]+nums[r];
                    if(sum < target){
                        l++;
                    }else if (sum > target){
                        r--;
                    }else{
                        List<Integer> t = new ArrayList<>();
                        t.add(nums[i]);
                        t.add(nums[j]);
                        t.add(nums[l]);
                        t.add(nums[r]);
                        ans.add(t);
                        l++;
                        r--;
                    }
                }
            }
        }
        return new ArrayList<>(ans);
    }
}
