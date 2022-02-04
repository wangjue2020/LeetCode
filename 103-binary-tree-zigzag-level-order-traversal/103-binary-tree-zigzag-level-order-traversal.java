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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        if (root == null) return ans;
        ArrayDeque<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        boolean left = true;
        while( !q.isEmpty()){
            ArrayList<Integer> cur_ans = new ArrayList<>();
            int size = q.size();
            for (int i = 0; i < size; i++){
                TreeNode cur = q.poll();
                if(left)
                    cur_ans.add(cur.val);
                else
                    cur_ans.add(0,cur.val);
                if(cur.left != null){
                    q.offer(cur.left);
                }
                if (cur.right != null){q.offer(cur.right);}
            }
            ans.add(cur_ans);
            left = !left;
        }
        return ans;
    }
}