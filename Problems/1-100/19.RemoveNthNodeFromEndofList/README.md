## [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)  
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
>Input: head = [1,2,3,4,5], n = 2  
Output: [1,2,3,5]  

Example 2:
>Input: head = [1], n = 1  
Output: []  

Example 3:
>Input: head = [1,2], n = 1  
Output: [1]  

**Solution**
* HashMap  
    用hashmap来记录每一个node的位置， 然后length - n +1 得到需要删除的是第几个node，然后做相应的next指针更新  
    Time Complexity: O(n)  
    Space Complexity: O(n)  
* Double Pointer 
    用两个指针，一个指针fast先移动，直到fast 指针与slow指针之间相差n个node，则当fast指针指到linkedList最后时，slow指向的则是要被删除的node。 
    Time Complexity: O(n)  
    Space Complexity: O(1)  