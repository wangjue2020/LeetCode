public class TwoSumIIInputArraySorted {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0;
        int r = numbers.length-1;
        while(l<r){
            int sum = numbers[l]+numbers[r];
            if(target>sum)
                l++;
            else if(target<sum)
                r--;
            else
                return new int[]{l+1, r+1};
        }
        return new int[2];
    }
}
