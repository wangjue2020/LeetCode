import java.util.HashMap;
import java.util.Map;

public class RemoveNthNodeFromEndOfList {
    /**
     * Use double pointer, one for fast, the other one is for slow
     * @param head
     * @param n
     * @return
     */
    public ListNode removeNthFromEnd1(ListNode head, int n) {
        ListNode fast = head;
        ListNode ans = new ListNode(-1, head);
        ListNode slow = ans;
        int count =0;
        while (fast != null && fast.next != null){
            if(count < n-1){
                fast = fast.next;
                count++;
            }else{
                slow = slow.next;
                fast = fast.next;
            }
        }
        if(head.next == null){
            return null;
        }
        slow.next= slow.next.next;
        return ans.next;
    }
    /**
     * Use HashMap
     * @param head
     * @param n
     * @return
     */
    @Deprecated
    public ListNode removeNthFromEnd(ListNode head, int n) {
        Map<Integer, ListNode> map = new HashMap<>();
        ListNode tmp = head;
        int i = 1;
        while (tmp != null){
            map.put(i, tmp);
            tmp = tmp.next;
            i++;
        }
        int ind = i-n;
        if(i == 2){
            return null;
        }
        if(n == i-1){
            return head.next;
        }
        map.get(ind-1).next = map.get(ind+1);
        return head;

    }
}
