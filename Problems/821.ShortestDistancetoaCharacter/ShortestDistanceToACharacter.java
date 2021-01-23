public class ShortestDistanceToACharacter {
    public int[] shortestToChar(String S, char C) {
        int[] ans = new int[S.length()];
        int pre = -2*S.length();
        for ( int i =0 ;i<S.length();i++){
            if(S.charAt(i) == C)
                pre = i;
            ans[i] = i-pre;
        }
        pre = 2*S.length();
        for(int i =S.length()-1; i>=0; i--){
            if(S.charAt(i) == C)
                pre = i;
            ans[i] = Math.min(ans[i], pre-i);
        }
        return ans;
    }
}
