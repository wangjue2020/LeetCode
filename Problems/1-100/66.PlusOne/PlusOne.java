public class PlusOne {
    public int[] plusOne(int[] digits) {
        int ind = digits.length-1;

        int f = 1;

        while (ind>=0 && f==1){
            int sum = digits[ind]+f;
            if (sum >=10){
                digits[ind] = sum%10;
                f = 1;
                ind--;
            }else{
                digits[ind] = sum;
                f=0;
            }
        }
        if(f==1){
            int[] ans = new int[digits.length+1];
            ans[0] = 1;
            for(int i = 1; i < ans.length; i++){
                ans[i] = digits[i-1];
            }
            return ans;
        }
        return digits;
    }
}
