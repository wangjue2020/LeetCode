##[141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's next pointer is connected to. Note that `pos` is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.  

Example :  
![cycled linked list](circularlinkedlist.png)  
>Input: head = [3,2,0,-4], pos = 1  
Output: true  
Explanation:  
There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).  

**Solution**  
快慢指针法：  
* 快慢指针法：  
    快指针每次跨两步，慢指针每次跨一步，直到快慢指针指向同一个位置时，则说明这个LinkedList存在Cycle， 之后用两个指针，一个指向刚刚重合的ListNode 一个指向head， 每次跨一步，直到重合，则当前ListNode一定是the node where the cycle begins.  
 Time Complexity: O(n)  