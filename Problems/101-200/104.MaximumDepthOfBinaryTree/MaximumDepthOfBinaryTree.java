import java.util.ArrayDeque;
import java.util.Queue;

public class MaximumDepthOfBinaryTree {
    /**
     * Divide and Conquer
     */
    public int maxDepthDC(TreeNode root) {
        if(root == null)
            return 0;
        int left = maxDepthDC(root.left);
        int right = maxDepthDC(root.right);

        return Math.max(left,right)+1;
    }
    /**
     * BFS
     */
    public int maxDepthBFS(TreeNode root) {
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

            }
        }
        return ans;
    }
}
