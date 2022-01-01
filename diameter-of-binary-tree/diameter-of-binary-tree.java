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
    public int diameter;
    public int diameterOfBinaryTree(TreeNode root) {
        this.dfs(root);
        return diameter-1;
    }
    public int dfs(TreeNode root){
        if (root == null)
            return 0;
        if (root.left == null && root.right == null){
            diameter = diameter > 1 ? diameter : 1;
            return 1;
        }
            
        else{
            int left = this.dfs(root.left);
            int right = this.dfs(root.right);
            diameter = left + right + 1 > diameter ? left + right + 1 : diameter;
            return left > right ? left+1 : right+1;
        }
    }
}