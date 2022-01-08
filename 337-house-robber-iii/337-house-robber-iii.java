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
    public int rob(TreeNode root) {
        int[] ans = this.dfs(root);
        return Math.max(ans[0], ans[1]);
    }
    public int[] dfs(TreeNode root){
        if (root==null) 
            return new int[]{0,0};
        if (root.left == null && root.right == null)
            return new int[]{root.val,0};
        else{
            int[] l = this.dfs(root.left);
            int[] r = this.dfs(root.right);
            int first = root.val + l[1] + r[1];
            int second = Math.max(l[0]+r[0], Math.max(l[1]+r[0], Math.max(l[0]+r[1], l[1]+r[1])));
            return new int[]{first, second};
        }
    }
 
            
}