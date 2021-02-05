import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class NaryTreePreorderTraversal {
    /**
     * Recursively
     * @param root
     * @return
     */
    public List<Integer> preorder1(Node root) {
        List<Integer> ans = new ArrayList<>();
        if(root == null)
            return ans;
        ans.add(root.val);
        for(Node n : root.children){
            ans.addAll(preorder(n));
        }
        return ans;
    }
    /**
     * Iteratively
     * @param root
     * @return
     */
    public List<Integer> preorder(Node root) {
        List<Integer> ans = new ArrayList<>();
        if(root == null)
            return ans;
        Stack<Node> stack = new Stack<>();
        stack.push(root);
        while(!stack.isEmpty()){
            Node last = stack.pop();
            ans.add(last.val);
            for(int i = last.children.size()-1; i>=0; i--){
                stack.push(last.children.get(i));
            }
        }
        return ans;
    }
}
