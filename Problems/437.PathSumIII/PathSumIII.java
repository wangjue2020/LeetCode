import java.util.ArrayList;
import java.util.List;

public class PathSumIII {
    private int a = 0;
    public int pathSum(TreeNode root, int sum) {
        pathSumHelper(root, sum);
        return a;
    }

    public List<Integer> pathSumHelper(TreeNode root, int sum){
        List<Integer> ans = new ArrayList<>();
        if(root == null)
            return ans;
        if(root.left == null && root.right == null){
            ans.add(root.val);
            if(root.val == sum)
                a++;
            return ans;
        }else{
            List<Integer> l = pathSumHelper(root.left, sum);
            List<Integer> r = pathSumHelper(root.right, sum);
            for(int i : l){
                if(i+root.val == sum)
                    a++;
                ans.add(i+root.val);
            }
            for(int i : r){
                if(i+root.val == sum)
                    a++;
                ans.add(i+root.val);
            }
            if(root.val == sum)
                a++;
            ans.add(root.val);
        }
        return ans;
    }
}
