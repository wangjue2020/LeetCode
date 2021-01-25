public class LongestPalindromicSubstring {
    int[][] dp;
    public String longestPalindrome(String s) {
        dp = new int[s.length()][s.length()];
        String ans = s.substring(0,1);
        for(int i = 0; i< s.length(); i++){
            String e1 = extend(i, i, s);
            String e2 = extend(i, i+1, s);
            if(Math.max(e1.length(), e2.length())>= ans.length())
                ans = e1.length()>e2.length()?e1:e2;
        }
        return ans;
    }
    public String extend(int i, int j, String s){
        while (i >=0 && j < s.length() && s.charAt(i)==s.charAt(j)){
            i--;
            j++;
        }
        return s.substring(i+1, j);
    }
}
