import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class NaryTreePostorderTraversal {
    /**
     * Iteratively
     * @param root
     * @return
     */
    public List<Integer> postorder1(Node root) {
        List<Integer> ans = new ArrayList<>();
        if(root == null){
            return ans;
        }
        Stack<Node> stack = new Stack<>();
        stack.push(root);
        while(!stack.isEmpty()){
            Node last = stack.pop();
            ans.add(last.val);
            for(Node n:last.children){
                stack.push(n);
            }
        }
        List<Integer> f = new ArrayList<>();
        for(int i =ans.size()-1; i >=0;i--){
            f.add(ans.get(i));
        }
        return f;
    }
    /**
     * Recursively
     * @param root
     * @return
     */
    public List<Integer> postorder(Node root) {
        List<Integer> ans = new ArrayList<>();
        if(root == null){
            return ans;
        }
        for(Node n: root.children){
            ans.addAll(postorder(n));
        }
        ans.add(root.val);
        return ans;
    }
}
