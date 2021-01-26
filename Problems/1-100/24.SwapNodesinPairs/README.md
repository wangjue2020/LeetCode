## [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)  
Given a linked list, swap every two adjacent nodes and return its head.

 

Example 1:
>Input: head = [1,2,3,4]  
Output: [2,1,4,3]  

Example 2:
>Input: head = []  
Output: []  

Example 3:
>Input: head = [1]  
Output: [1]  

**Solution**
* LinkedList
    交换对应指针， 加一个伪node作为开头避免prev指针指向null。  
    Time Complexity: O(n);