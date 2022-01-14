/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null){return head;}
        ListNode fast = head;
        ListNode slow = head;
        boolean start = true;
        ListNode meet = null;
        while (fast != null && fast.next != null){
            if (fast == slow && !start){
                meet = fast;
                break;
            }
            start=false;
            fast = fast.next.next;
            slow = slow.next;
        }
        if (meet == null){
            return null;
        } else {
            ListNode pt1 = head;
            while(pt1!=meet){
                pt1 = pt1.next;
                meet = meet.next;
            }
            return meet;
        }
    }
}