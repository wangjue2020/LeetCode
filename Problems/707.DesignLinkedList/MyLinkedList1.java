public class MyLinkedList1 {
    /**
     * using general linked list
     */
    ListNode head = null;
    int size;
    /** Initialize your data structure here. */
    public MyLinkedList1() {
        head = new ListNode(-1);
        size = 0;
    }

    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    public int get(int index) {
        if(index < 0 || index >= size){
            return -1;
        } else{
            ListNode temp = head;
            for ( int i = 0; i<=index; i++){
                temp = temp.next;
            }
            return temp.val;
        }
    }

    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    public void addAtHead(int val) {

        ListNode n = new ListNode(val, head.next);
        head.next = n;
        size++;

    }

    /** Append a node of value val to the last element of the linked list. */
    public void addAtTail(int val) {
        addAtIndex(size,val);
    }

    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    public void addAtIndex(int index, int val) {
        if(index > size){
            return;
        }else{
            ListNode temp = head;
            for ( int i = 0; i<index ;i++){
                temp = temp.next;
            }
            ListNode n = new ListNode(val, temp.next);
            temp.next = n;
            size++;
        }

    }

    /** Delete the index-th node in the linked list, if the index is valid. */
    public void deleteAtIndex(int index) {
        if ( index < 0 || index >= size){
            return;
        }else{
            ListNode temp = head;
            for ( int i =0; i< index; i++){
                temp = temp.next;
            }
            System.out.println(temp.val+":"+temp.next.val);
            temp.next  = temp.next.next;
            size--;
        }
    }

    class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
}
