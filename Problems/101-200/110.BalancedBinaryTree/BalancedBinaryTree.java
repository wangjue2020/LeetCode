public class BalancedBinaryTree {
    public boolean isBalanced(TreeNode root) {
        if ( root ==null)
            return true;
        int[] res = isBalanced1(root);
        return res[0] ==1?true:false;
    }
    public int[] isBalanced1(TreeNode root){
        if(root == null)
            return new int[]{1,0};
        int ans = 0;
        int[] left = isBalanced1(root.left);
        int[] right = isBalanced1(root.right);
        if(left[0] == 0 || right[0] == 0)
            return new int[]{0,0};
        if(Math.abs(right[1]-left[1]) > 1)
            return new int[]{0, Math.max(left[1], right[1])+1};
        else{
            return new int[]{1, Math.max(left[1], right[1])+1};
        }
    }
}
