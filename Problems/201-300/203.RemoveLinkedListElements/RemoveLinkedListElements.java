public class RemoveLinkedListElements {
    public ListNode removeElements(ListNode head, int val) {
        ListNode pre = null;
        ListNode temp = head;
        while (temp != null) {
            if (temp.val == val){
                if(temp == head){
                    head = head.next;
                    temp = head;
                }else{
                    pre.next = temp.next;
                    temp = temp.next;
                }
            }else{
                pre = temp;
                temp = temp.next;
            }
        }
        return head;
    }

    /**
     * 方法二
     * @param head
     * @param val
     * @return
     */
    public ListNode removeElements1(ListNode head, int val) {
        ListNode temp = head;
        ListNode dummyNode = new ListNode(-1, head);
        ListNode pre = dummyNode;
        while (temp != null) {
            if (temp.val == val){
                pre.next = temp.next;
                temp = temp.next;
            }else{
                pre = temp;
                temp = temp.next;
            }
        }
        return dummyNode.next;
    }
}

class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }

    @Override
    public String toString() {
        return "ListNode{" +
                "val=" + val +
                ", next=" + next +
                '}';
    }
}
