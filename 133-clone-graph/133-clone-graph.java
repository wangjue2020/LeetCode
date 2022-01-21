/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        Node ans = this.dfs(node);
        // System.out.println(ans.val);
        // System.out.println(ans.neighbors.toString());
        return ans;
    }
    public Node dfs(Node node){
        if (node == null) 
            return node;
        Map<Integer, Node> map = new HashMap<>();
        Set<Integer> set = new HashSet<>();
        LinkedList<Node> s = new LinkedList<>();
        s.offer(node);
        Node ans = new Node(node.val);
        LinkedList<Node> snew = new LinkedList<>();
        snew.offer(ans);
        map.put(node.val, ans);
            
        while(!s.isEmpty()){
            Node cur = s.poll();
            Node ptr = snew.poll();
            if (set.contains(cur.val)){
                // System.out.println("pass");
                continue;
            }
            for (Node e: cur.neighbors){
                
                Node new_node =map.getOrDefault(e.val, new Node(e.val));
                ptr.neighbors.add(new_node);
                s.offer(e);
                snew.offer(new_node);
                map.put(e.val, new_node);
            }
            set.add(cur.val);
            
        }
        return ans;
    }
}