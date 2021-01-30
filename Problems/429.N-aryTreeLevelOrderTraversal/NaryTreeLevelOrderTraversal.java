import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

public class NaryTreeLevelOrderTraversal {
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> ans = new ArrayList<>();
        if (root == null)
            return ans;
        Queue<Node> q = new ArrayDeque<>();
        q.offer(root);
        while(q.size()!= 0){
            List<Integer> cur = new ArrayList<>();
            int size = q.size();
            for(int i =0; i < size; i++){
                Node n = q.poll();
                cur.add(n.val);
                q.addAll(n.children);
            }
            ans.add(cur);
        }
        return ans;
    }
}
