public class InvertBinaryTree {
    public TreeNode invertTree(TreeNode root) {
        if(root == null)
            return root;
        if(root.left == null && root.right == null)
            return root;
        else if(root.left == null && root.right != null){
            root.left = invertTree(root.right);
            root.right=null;

        }else if(root.right == null && root.left != null){
            root.right = invertTree(root.left);
            root.left = null;
        }else{
            TreeNode tmp = root.left;
            root.left = invertTree(root.right);
            root.right = invertTree(tmp);
        }
        return root;
    }
}
