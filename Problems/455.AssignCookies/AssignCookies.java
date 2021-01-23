import java.util.Arrays;

public class AssignCookies {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int ans = 0;
        int j =0;
        for(int i=0; i < s.length && j < g.length; i++){
            if(s[i] >= g[j]){
                ans++;
                j++;
            }
        }
        return ans;
    }
}
