import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class BinaryTreeInorderTraversal {
    /**
     * Iterative Mthode
     * @param root
     * @return
     */
    public List<Integer> inorderTraversal1(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        if(root == null)
            return ans;
        Stack<TreeNode> stack = new Stack<>();
        while (root!= null || !stack.isEmpty()){
            while(root != null ){
                stack.push(root);
                root= root.left;
            }
            root = stack.pop();
            ans.add(root.val);
            root = root.right;
        }
        return ans;
    }
    /**
     * Recursion
     * @param root
     * @return
     */
    public List<Integer> inorderTraversal(TreeNode root) {
        if(root == null){
            return new ArrayList<Integer>();
        }
        List<Integer> ans = new ArrayList<>();
        List<Integer> left = inorderTraversal(root.left);
        List<Integer> right = inorderTraversal(root.right);
        ans.addAll(left);
        ans.add(root.val);
        ans.addAll(right);
        return ans;
    }
}
