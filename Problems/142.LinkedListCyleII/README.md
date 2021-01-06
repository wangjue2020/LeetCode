## [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
 
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, `pos` is used to denote the index of the node that tail's next pointer is connected to. Note that `pos` is not passed as a parameter.

Notice that you should not modify the linked list  

Example 1:  
 ![cycled linked list](../142.LinkedListCyleII/circularlinkedlist.png)
> Input: head = [3,2,0,-4], pos = 1  
  Output: tail connects to node index 1  
  Explanation:  
  There is a cycle in the linked list, where tail connects to the second node.
  

**Solution**  
* 解法一：
    用ArrayList或者其他collection来已经经过的ListNode， check是否contains，第一次出现contain的ListNode则是the node where cycle begins.  
    The time complexity of HashSet conatins()  is O(1).  
    
   Time Complexity: O(n)  
* 快慢指针法：  
    快指针每次跨两步，慢指针每次跨一步，直到快慢指针指向同一个位置时，则说明这个LinkedList存在Cycle， 之后用两个指针，一个指向刚刚重合的ListNode 一个指向head， 每次跨一步，直到重合，则当前ListNode一定是the node where the cycle begins.  
    
    假设从head到环形入口node的节点数为x， 从环形入口处到快慢指针相遇的节点的节点数为y，从快慢指针相遇的节点到环形入口处的节点数为z  
    则慢指针走过x+y个节点，快指针走过x + y+ n(y+z), 因为快指针走过的节点数是慢指针的两倍，所以，2*(x+y) = x+y +n(x+y)得到x=(n-1)(y+z)+z, 其中从相遇节点到环形入口需要z，然后y+z是环形总长度。
    说明从头结点出发一个指针，从相遇节点 也出发一个指针，这两个指针每次只走一个节点， 那么当这两个指针相遇的时候就是 环形入口的节点  
    
    
