import java.util.LinkedList;
import java.util.Queue;

public class SymmetricTree {
    /**
     * Iteration
     * @param root
     * @return
     */
    public boolean isSymmetricIteration(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        q.add(root);
        while (!q.isEmpty()){
            TreeNode l = q.poll();
            TreeNode r = q.poll();
            if(l == null && r == null) continue;
            if(l == null || r == null || l.val!=r.val)
                return false;
            else{
                q.add(l.left);
                q.add(r.right);
                q.add(l.right);
                q.add(r.left);
            }

        }
        return true;
    }
    /**
     * Recursion
     * @param root
     * @return
     */
    public boolean isSymmetricRecursion(TreeNode root) {
        if(root == null)
            return true;
        else{
            return rec(root.left, root.right);
        }
    }
    public boolean rec(TreeNode l, TreeNode r){
        if(l == null && r == null)
            return true;
        if(l == null || r == null || l.val != r.val)
            return false;
        else{
            return rec(l.left, r.right) && rec(l.right, r.left);
        }
    }
}
