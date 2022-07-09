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
        if (head == null || head.next == null)
            return head;
        ListNode mid = computeMid(head);
        ListNode left = sortList(head);
        ListNode right = sortList(mid);
        return merge(left, right);
    }
    
    ListNode computeMid(ListNode head){
        ListNode p = null;
        while(head != null && head.next != null){
            p = (p == null)? head: p.next;
            head = head.next.next;
        }
        ListNode mid = p.next;
        p.next = null;
        return mid;
    }
    
    ListNode merge(ListNode l1, ListNode l2){
        ListNode ans = new ListNode(-1);
        ListNode ptr = ans;
        while(l1 != null && l2 != null){
            if (l1.val < l2.val){
                ptr.next = l1;
                l1 = l1.next;
                ptr = ptr.next;
            }else{
                ptr.next = l2;
                l2 = l2.next;
                ptr = ptr.next;
            }
        }
        ptr.next = (l1 != null) ? l1:l2;
        return ans.next;
    }
}