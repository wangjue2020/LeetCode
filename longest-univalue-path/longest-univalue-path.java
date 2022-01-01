/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int ans;
    public int longestUnivaluePath(TreeNode root) {
        if (root == null) return 0;
        this.dfs(root);
        return ans-1;
    }
    public int dfs(TreeNode root){
        if (root == null){ return 0;}
        if (root.left == null && root.right == null) {
            this.ans = ans > 1 ? ans : 1;
            return 1;
        }else{
            int left = this.dfs(root.left);
            int right = this.dfs(root.right);
            int cur_l = 1;
            if (left != 0 && root.val == root.left.val)
                cur_l += left;
            int cur_r = 1;
            if(right != 0 && root.val == root.right.val)
                cur_r += right;
            int cur_r_l = 1;
            if (right != 0 && left != 0 && root.val == root.left.val && root.val == root.right.val)
                cur_r_l = cur_r + cur_l -1;
            int max = Math.max(cur_l, Math.max(cur_r, cur_r_l));
            this.ans = Math.max(max, this.ans);
            return cur_r > cur_l ? cur_r : cur_l;
        }
    }
}