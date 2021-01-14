import java.util.ArrayDeque;
import java.util.Queue;

public class MinimumDepthOfBinaryTree {
    /**
     * BFS (performs better than divider and conquer)
     * @param root
     * @return
     */
    public int minDepth(TreeNode root) {
        if(root==null)
            return 0;
        int ans = 0;
        Queue<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        while(!q.isEmpty()){
            int size = q.size();
            ans++;
            for(int i =0;i<size; i++){
                TreeNode cur = q.remove();
                if(cur.left!=null){
                    q.add(cur.left);
                }
                if(cur.right != null){
                    q.add(cur.right);
                }
                if(cur.left == null && cur.right==null){
                    return ans;
                }

            }
        }
        return ans;
    }

    /**
     * Divide and Conquer
     * @param root
     * @return
     */
    public int minDepthDC(TreeNode root) {
        if(root == null)
            return 0;
        int left = minDepthDC(root.left);
        int right = minDepthDC(root.right);

        if(left != 0 && right != 0)
            return Math.min(left, right)+1;
        if(left ==0){
            return right+1;
        }else{
            return left+1;
        }
    }
}
