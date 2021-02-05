import java.util.ArrayDeque;
import java.util.Queue;

public class DeepestLeavesSum {
    public int deepestLeavesSum(TreeNode root) {
        Queue<TreeNode> q = new ArrayDeque<TreeNode>();
        if(root==null)
            return 0;
        Integer ans = 0;
        q.offer(root);
        while(0!=q.size()){
            int tmp = 0;
            int size = q.size();
            for(int i =0; i<size; i++){
                TreeNode cur = q.poll();
                if(cur.left == null && cur.right == null)
                    tmp += cur.val;
                if(cur.left != null)
                    q.offer(cur.left);
                if(cur.right != null)
                    q.offer(cur.right);
            }
            ans = tmp;
        }
        return ans;
    }
}
