import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

public class GenerateParentheses {
    /**
     * DFS
     * @param n
     * @return
     */
    public List<String> generateParenthesis1(int n) {
        List<String> ans = new ArrayList();
        backtrack(ans, "", 0, 0, n);
        return ans;
    }

    public void backtrack(List<String> ans, String cur, int open, int close, int max){
        if (cur.length() == max * 2) {
            ans.add(cur);
            return;
        }

        if (open < max)
            backtrack(ans, cur+"(", open+1, close, max);
        if (close < open)
            backtrack(ans, cur+")", open, close+1, max);
    }
    /**
     * BFS
     * @param n
     * @return
     */
    public List<String> generateParenthesis(int n) {
        Queue<String> ans = new ArrayDeque<>();
        Queue<int[]> help = new ArrayDeque<>();
        List<String> list = new ArrayList<>();
        ans.add("(");
        help.add(new int[]{n-1, n});
        boolean f= true;
        while(ans.size()>0){
            int size = ans.size();
            for(int i =0; i<size; i++){
                String cur = ans.poll();
                int[] count = help.poll();
                if(count[0] > 0){
                    ans.add(cur+"(");
                    help.add(new int[]{count[0]-1, count[1]});
                }
                if(count[1]>0){
                    if(count[0] < count[1]){
                        if(count[0]==0 && count[1]-1==0){
                            list.add(cur+")");
                        }else{
                            ans.add(cur+")");
                            help.add(new int[]{count[0], count[1]-1});
                        }
                    }
                }
            }
        }
        return list;
    }
}
