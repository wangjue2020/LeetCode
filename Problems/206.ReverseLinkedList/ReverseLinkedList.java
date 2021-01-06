public class ReverseLinkedList {
    public ListNode reverseList(ListNode head) {
        ListNode pre = null;
        ListNode temp = head;
        if(temp == null)
            return head;
        while (temp.next != null){
            ListNode n = temp.next;
            temp.next = pre;
            pre = temp;
            temp = n;
        }
        temp.next= pre;
        return temp;
    }
}
