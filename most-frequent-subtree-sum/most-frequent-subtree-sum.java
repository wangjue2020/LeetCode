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
    
    public Map<Integer, Integer> map_sum_count = new HashMap<>();
    public Map<Integer, List<Integer>> map_count_sum = new HashMap<>();
    public int max_count = 0;
    public int[] findFrequentTreeSum(TreeNode root) {
        this.dfs(root);
        System.out.println(map_sum_count.toString());
        System.out.println(map_count_sum.toString());
        List<Integer> ans = map_count_sum.get(max_count);
        int[] answer = new int[ans.size()];
        for(int i=0; i< ans.size(); i++){
            answer[i] = ans.get(i);
        }
        
        return answer;
    }
    public int dfs(TreeNode root){
        if (root == null) return 0;
        int cur_sum = 0;
        int count = 0;
        if(root.left == null && root.right == null){
            cur_sum = root.val;
            count = map_sum_count.getOrDefault(cur_sum, 0);
            map_sum_count.put(cur_sum, ++count);
            List<Integer> sum_array = map_count_sum.getOrDefault(count, new ArrayList<Integer>());
            sum_array.add(cur_sum);
            map_count_sum.put(count, sum_array);
            max_count = count > max_count ? count : max_count;
        }else{
            int left = this.dfs(root.left);
            int right = this.dfs(root.right);
            cur_sum = left + right + root.val;
            count = map_sum_count.getOrDefault(cur_sum, 0);
            map_sum_count.put(cur_sum, ++count);
            List<Integer> sum_arrays = map_count_sum.getOrDefault(count, new ArrayList<Integer>());
            sum_arrays.add(cur_sum);
            map_count_sum.put(count, sum_arrays);
            max_count = count > max_count ? count : max_count;
        }
        return cur_sum;
    }
}