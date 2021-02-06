import java.util.ArrayDeque;
import java.util.Queue;

public class SubtreeOfAnotherTree {
    /**
     * BFS + Recursive
     * @param s
     * @param t
     * @return
     */
    public boolean isSubtree1(TreeNode s, TreeNode t) {
        if(s == null && t == null)
            return true;
        if(s == null || t == null)
            return false;
        Queue<TreeNode> q = new ArrayDeque<>();
        q.add(s);
        while(q.size()!=0){
            int size = q.size();
            for(int i =0; i< size; i++){
                TreeNode cur = q.poll();
                if(cur.val == t.val){
                    if(isSameTree(cur, t))
                        return true;
                }
                if(cur.left != null)
                    q.add(cur.left);
                if(cur.right != null)
                    q.add(cur.right);
            }
        }
        return false;
    }
    public boolean isSameTree(TreeNode t1, TreeNode t2){
        if(t1==null && t2==null)
            return true;
        if(t1 != null && t2 == null)
            return false;
        if(t2 != null && t1 == null)
            return false;
        if(t1.val == t2.val)
            return isSameTree(t1.left, t2.left) && isSameTree(t1.right, t2.right);
        else
            return false;
    }
    /**
     * Preorder
     * @param s
     * @param t
     * @return
     */
    public boolean isSubtree(TreeNode s, TreeNode t) {
        String s1 = preorder(s,true);
        String s2 = preorder(t,true);
        return s1.contains(s2);
    }
    public String preorder(TreeNode t, boolean l){
        if(t==null)
            return l?"lnull":"null";
        String s ="#";
        s +=String.valueOf(t.val);
        s+=preorder(t.left, true);
        s+=preorder(t.right, false);
        return s;
    }
}
