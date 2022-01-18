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
    public ListNode sortList(ListNode head) {
        PriorityQueue<ListNode> pq = new PriorityQueue<>(new Comparator<ListNode>(){
            @Override
            public int compare(ListNode n1, ListNode n2){
                if (n1.val < n2.val){
                    return -1;
                }else if (n1.val == n2.val){return 0;}
                else{return 1;}
            }
        });
        while (head != null){
            pq.offer(head);
            head = head.next;
        }
        ListNode ans = new ListNode(-1);
        head = ans;
        while(pq.size()!= 0){
            head.next = pq.poll();
            head = head.next;
        }
        head.next = null;
        return ans.next;
    }
}