public class LongestSubstringWithoutRepeatingCharacters {
    public int lengthOfLongestSubstring(String s) {
        String ans = "";
        int start = 0;
        int f = 0;
        for (int i =0; i<s.length();i++){
            String cur = s.substring(i,i+1);
            if(!ans.contains(cur)){
                ans+=cur;

            }else{
                int ind = ans.indexOf(cur);
                start = start+ind+1;
                f = f>= ans.length()? f: ans.length();
                ans = ans.substring(ind+1)+cur;
            }
        }
        if(ans.equals(s))
            return ans.length();
        return f>= ans.length()? f: ans.length();
    }
}
