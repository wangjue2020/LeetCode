import java.util.Stack;

public class LeafSimilarTrees {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        String s1 = getLeafSequence(root1);
        String s2 = getLeafSequence(root2);
        return s1.equals(s2);
    }
    public String getLeafSequence(TreeNode root){
        String ans = "";
        if(root == null)
            return ans;
        Stack<TreeNode> s = new Stack<>();
        while(root != null ||!s.empty()){
            while(root != null){
                s.push(root);
                root = root.left;
            }
            root = s.pop();
            if(root.left == null && root.right == null)
                ans += "#"+String.valueOf(root.val);
            root = root.right;
        }
        return ans;
    }
}
