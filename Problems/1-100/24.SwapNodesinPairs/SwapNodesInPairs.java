public class SwapNodesInPairs {
    public ListNode swapPairs(ListNode head) {
        ListNode tmp = new ListNode(-1, head);
        if(head == null || head.next == null)
            return head;
        ListNode pre = tmp;
        while (head!= null && head.next != null){
            ListNode next = head.next;
            pre.next = head.next;
            head.next = next.next;
            next.next = head;
            pre = head;
            head = head.next;

        }
        return tmp.next;
    }
}
