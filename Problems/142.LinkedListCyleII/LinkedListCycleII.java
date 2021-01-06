import java.util.HashSet;

public class LinkedListCycleII {
    /**
     * 快慢指针法
     */
    public ListNode detectCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        boolean f = false;
        while (slow != null && slow.next != null && fast!=null & fast.next != null && fast.next.next !=null){
            if(fast == slow && f){
                ListNode n1 = head;
                ListNode n2 = fast;
                while (n1!=n2){
                    n1 = n1.next;
                    n2=n2.next;
                }
                return n1;
            }else{
                f= true;
                slow = slow.next;
                fast = fast.next.next;
            }
        }
        return null;
    }
    /**
     * 用collection记录走过的ListNode方法
     */
    public ListNode detectCycle1 (ListNode head) {
        HashSet<ListNode> set = new HashSet<>();
        while(head != null){
            if(set.contains(head))
                return head;
            else{
                set.add(head);
                head =head.next;
            }
        }
        return null;
    }
}
