public class LinkedListCycle {
    public boolean hasCycle(ListNode head) {
        if(head == null){
            return false;
        }
        ListNode slow = head;
        ListNode fast = head.next;
        while(fast != slow){
            if(fast == null || fast.next == null){
                return false;
            } else {
                fast = fast.next.next;
                slow = slow.next;
            }
        }
        return true;
    }
}
