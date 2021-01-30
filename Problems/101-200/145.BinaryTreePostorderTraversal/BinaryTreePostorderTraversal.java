import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class BinaryTreePostorderTraversal {
    /**
     * Iterative
     * @param root
     * @return
     */
    public List<Integer> postorderTraversal1(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        Stack<TreeNode> s = new Stack<>();
        if(root == null)
            return ans;
        s.push(root);
        while(s.size()!=0){
            TreeNode cur = s.pop();
            ans.add(cur.val);
            if(cur.left != null)
                s.push(cur.left);
            if(cur.right != null)
                s.push(cur.right);

        }
        List<Integer> rev = new ArrayList<>();
        for(int i =ans.size()-1; i>=0; i--){
            rev.add(ans.get(i));
        }
        return rev;
    }
    /**
     * recursion
     * @param root
     * @return
     */
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        if(root == null)
            return ans;
        List<Integer> left = postorderTraversal(root.left);
        List<Integer> right = postorderTraversal(root.right);

        ans.addAll(left);
        ans.addAll(right);
        ans.add(root.val);
        return ans;
    }
}
