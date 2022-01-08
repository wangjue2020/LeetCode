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
    public int distributeCoins(TreeNode root) {
        int[] ans = this.dfs(root);
        return ans[1];
    }
    public int[] dfs(TreeNode root){
        if (root == null){return new int[]{0,0};}
        if (root.left == null && root.right == null){
            if(root.val == 0)
                return new int[]{-1,1};
            else
                return new int[]{root.val-1,Math.abs(root.val-1-0)};
        }
        else{
            int[] l = this.dfs(root.left);
            int[] r = this.dfs(root.right);
            int first = l[0]+r[0]-1+root.val;
            int second = l[1]+r[1] + Math.abs(first-0);
            return new int[]{first, second};
        }
    }
}