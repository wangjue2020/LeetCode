/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        String s = "";
        if (root == null) return s;
        LinkedList ll = new LinkedList();
        ll.offer(root);
        int level = 0;
        while(!ll.isEmpty()){
            int size = ll.size();
            for (int i = 0; i < size; i++){
                Object tmp = ll.poll();
                if (tmp instanceof TreeNode){
                    TreeNode cur = (TreeNode) tmp;
                    s += cur.val+"/";
                    if (cur.left != null){
                        ll.offer(cur.left);
                    }else{
                        
                        ll.offer(null);
                    }
                    if (cur.right != null){
                        ll.offer(cur.right);
                    }else{
                        ll.offer(null);
                    }
                }else{
                    s += "A/";
                }
            }
            // if (countNull == Math.pow(2,level+1)){
            //     // System.out.println(s);
            //     return s;
            // }
            level++;
        }
        s = s.replaceAll("(A/)+$", "");
        System.out.println(s);
        return s;
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if ("".equals(data)) return null;
        LinkedList<TreeNode> ll = new LinkedList<>();
        int i = 0;
        String root_char = data.substring(i,++i);
        String root_s = "";
        while (! "/".equals(root_char) ){
            root_s += root_char;
            root_char = data.substring(i,++i);
        }
        TreeNode root = new TreeNode(Integer.parseInt(root_s));
        ll.offer(root);
        boolean flag = true;
        TreeNode parent = null;
        while (i < data.length()){
            String cur_char = data.substring(i, ++i);
            String cur_s = "";
            while(!"/".equals(cur_char)){
                cur_s += cur_char;
                cur_char = data.substring(i, ++i);
            }
            TreeNode cur = null;
            if(!"A".equals(cur_s)){
                cur = new TreeNode(Integer.parseInt(cur_s));

            }
            if (flag){
                parent = ll.poll();
                if (cur != null){
                    parent.left = cur;
                    ll.offer(cur);
                }
                flag = false;
            }else{
                if (cur != null){
                    parent.right = cur;
                    ll.offer(cur);
                }
                parent = null;
                flag = true;
            }
            

        }
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));
// [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]