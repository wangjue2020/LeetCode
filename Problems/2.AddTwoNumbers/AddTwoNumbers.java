import org.junit.Test;

import java.util.List;

public class AddTwoNumbers {
    @Test
    public  void test(){
        ListNode a = new ListNode(9, new ListNode(9, new ListNode(1)));
        ListNode listNode = addTwoNumbers(a, new ListNode(1));
        System.out.println(listNode);
    }
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ans = new ListNode(-1);
        ListNode temp = ans;
        int bit = 0;
        while (l1 != null && l2 != null){
            System.out.println(l1.val + ":" + l2.val + ":" + bit);
            int sum = l1.val + l2.val + bit;
            if(sum >=10){
                bit = 1;
            }else{
                bit = 0;
            }
            temp.next = new ListNode(sum%10);
            temp = temp.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        System.out.println(bit+":"+ans);
        System.out.println(l1);
        System.out.println(l2);
        if(l1 != null){
            while(l1!= null){
                System.out.println(bit+":"+ans);
                int sum = l1.val + bit;
                System.out.println(sum);
                if(sum >= 10){
                    bit = 1;
                    temp.next = new ListNode(sum%10);
                    temp =temp.next;
                    l1 = l1.next;
                }else{
                    temp.next = new ListNode(sum%10);
                    temp= temp.next;
                    bit = 0;
                    temp.next = l1.next;
                    break;
                }
            }
        }
        if(l2 != null){
            while(l2!= null){
                System.out.println(ans);
                int sum = l2.val + bit;
                if(sum >= 10){
                    bit = 1;
                    temp.next = new ListNode(sum%10);
                    temp =temp.next;
                    l2 = l2.next;
                }else{
                    temp.next = l2.next;
                    break;
                }
            }
        }
        if(bit == 1){
            temp.next = new ListNode(1);
        }
        return ans.next;
    }
}
