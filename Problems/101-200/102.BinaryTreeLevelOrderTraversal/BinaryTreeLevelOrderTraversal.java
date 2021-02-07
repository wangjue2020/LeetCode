import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class BinaryTreeLevelOrderTraversal {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        if(root == null)
            return ans;
        LinkedList<TreeNode> ll = new LinkedList<>();
        ll.offer(root);
        while(!ll.isEmpty()){
            int size = ll.size();
            List<Integer> tmp = new ArrayList<>();
            for(int i=0; i< size; i++){
                TreeNode cur = ll.poll();
                tmp.add(cur.val);
                if(cur.left!=null)
                    ll.offer(cur.left);
                if(cur.right != null)
                    ll.offer(cur.right);
            }
            ans.add(tmp);
        }
        return ans;
    }
}
