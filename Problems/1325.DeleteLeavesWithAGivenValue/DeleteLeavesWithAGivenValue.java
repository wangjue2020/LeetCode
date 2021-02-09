public class DeleteLeavesWithAGivenValue {
    TreeNode root;
    public TreeNode removeLeafNodes(TreeNode root, int target) {
        this.root = root;
        boolean f = checkLeaf(this.root,target);
        return f?null:this.root;
    }
    public boolean checkLeaf(TreeNode root, int target){
        if(root == null){
            return true;
        }
        if(root.left == null && root.right == null){
            return root.val == target;
        }
        boolean l = checkLeaf(root.left,target);
        boolean r = checkLeaf(root.right,target);
        if(l && r){
            root.left = null;
            root.right = null;
            return root.val==target;
        }
        if(l){
            root.left = null;
            return false;
        }
        if(r){
            root.right = null;
            return false;
        }
        if(!l && !r)
            return false;
        return false;
    }
}
