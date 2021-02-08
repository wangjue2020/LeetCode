public class BinaryTreePruning {
    TreeNode root;
    public TreeNode pruneTree(TreeNode root) {
        this.root = root;
        boolean res = checkTreeNode(this.root);
        return res?this.root:null;
    }
    public boolean checkTreeNode(TreeNode root){

        if(root == null)
            return true;
        if(root.left == null && root.right == null)
            return root.val == 1;
        boolean l = checkTreeNode(root.left);
        boolean r = checkTreeNode(root.right);
        if(l && r){
            return true;
        }else{
            if(!l && r){
                root.left = null;
                if(root.right == null)
                    return root.val==1;
                return true;
            }else if (!r && l){
                root.right = null;
                if(root.left == null)
                    return root.val==1;
                return true;
            }else{
                root.left = null;
                root.right =null;
                return root.val ==1;
            }
        }

    }
}
