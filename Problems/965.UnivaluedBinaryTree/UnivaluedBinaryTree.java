import java.util.LinkedList;

public class UnivaluedBinaryTree {
    /**
     * iteratively
     * @param root
     * @return
     */
    public boolean isUnivalTree(TreeNode root) {
        if(root == null)
            return true;
        LinkedList<TreeNode> ll = new LinkedList<>();
        ll.offer(root);
        int ans = root.val;
        while (!ll.isEmpty()){
            int size = ll.size();
            for(int i =0; i<size; i++){
                TreeNode cur = ll.poll();
                if(cur.val != ans)
                    return false;
                if(cur.left != null)
                    ll.offer(cur.left);
                if(cur.right != null)
                    ll.offer(cur.right);
            }
        }
        return true;
    }

    /**
     * recursively
     */
    int value;
    @Deprecated
    public boolean isUnivalTree1(TreeNode root) {
        // if(root == null)
        //     return true;
        value = root.val;
        return isUnivalTreeHelper(root);
    }
    public boolean isUnivalTreeHelper(TreeNode root){
        if(root == null)
            return true;
        System.out.println(root.val+":"+value);
        if(root.val == value)
            return isUnivalTreeHelper(root.left) && isUnivalTreeHelper(root.right);
        else
            return false;
    }
}
