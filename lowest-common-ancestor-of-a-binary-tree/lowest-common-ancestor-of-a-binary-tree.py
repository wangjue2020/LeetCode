/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        LinkedList<TreeNode> linkedlist = new LinkedList<>();
        linkedlist.offer(root);
        int lower = p.val > q.val ? q.val : p.val;
        int higher = p.val < q.val ? q.val : p.val;
        while(!linkedlist.isEmpty()){
            TreeNode cur = linkedlist.poll();
            if ((cur.val > lower && cur.val < higher) || (cur.val == lower) || (cur.val == higher)){
                return cur;
            } else{
                if (cur.left != null)
                    linkedlist.offer(cur.left);
                if (cur.right != null)
                    linkedlist.offer(cur.right);
            }
        }
        return null;
    }
}
