public class ReverseStringII {
    public String reverseStr(String s, int k) {
        if(k <= 0)
            return null;
        if(k==1)
            return s;
        int i =0;
        String ans = "";
        int length = s.length();
        while (i < length){

            if(length-i >= k){
                String result = reverseStr(s.substring(i, i+k));
                String rest  = "";
                if((i+2*k) <length){
                    rest = s.substring(i+k, i+2*k);
                    ans = ans+result+rest;
                    i = i+2*k;
                } else {
                    rest = s.substring(i+k);
                    ans = ans+result+rest;
                    return ans;
                }
            }else{
                String result = reverseStr(s.substring(i));
                return ans+result;
            }
        }
        return ans;
    }
    public String reverseStr(String s){
        String ans = "";
        for(int i = s.length()-1; i>=0 ; i--){
            ans += s.substring(i,i+1);
        }
        return ans;
    }
}
