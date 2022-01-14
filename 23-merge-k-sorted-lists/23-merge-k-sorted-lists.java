/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 0) return null;
        if (lists.length == 1) return lists[0];
        PriorityQueue<ListNode> pq = new PriorityQueue<>(new Comparator<ListNode>(){
            @Override
            public int compare (ListNode n1, ListNode n2){
                if (n1.val<n2.val){return -1;}
                else if (n1.val == n2.val){return 0;}
                else {return 1;}
            }
        });
        
        for (int i = 0; i < lists.length; i++){
            if (lists[i] != null )
                pq.offer(lists[i]);
        }
        // System.out.println(pq.toString());
        ListNode ans = new ListNode(-1);
        ListNode ptr = ans;
        while(pq.size()!=0){
            ListNode cur = pq.poll();
            ptr.next = cur;
            // System.out.println(pq.toString());
            if (cur.next!=null)
                pq.offer(cur.next);
            ptr = ptr.next;
        }
        return ans.next;
    }
}