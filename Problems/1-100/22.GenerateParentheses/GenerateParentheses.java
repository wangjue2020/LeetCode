import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

public class GenerateParentheses {
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
