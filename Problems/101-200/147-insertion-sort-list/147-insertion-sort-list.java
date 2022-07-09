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
    public ListNode insertionSortList(ListNode head) {
        ListNode ans = null;
        ListNode backup = null;
        while (head != null){
            if (ans == null){
                backup = head.next;
                ans = head;
                ans.next = null;
                head = backup;
            }else{
                if (head.val <= ans.val){
                    backup = head.next;
                    head.next = ans;
                    ans = head;
                    head = backup;
                }else{
                    ListNode ptr = ans;
                    ListNode p = null;
                    while(ptr!= null){
                        if (head.val > ptr.val){
                            p = ptr;
                            ptr = ptr.next;
                        }else{
                            backup = head.next;
                            p.next = head;
                            head.next = ptr;
                            head = backup;
                            break;
                        }
                    }
                    if (ptr == null){
                        p.next = head;
                        backup = head.next;
                        head.next = null;
                        head = backup;
                    }
                    
                }
            }
        }
        return ans;
    }
}