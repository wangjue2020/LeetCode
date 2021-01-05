## [707. Design Linked List](https://leetcode.com/problems/design-linked-list/submissions/)
 
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: `val` and `next`. `val` is the value of the current node, and `next` is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute `prev` to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the `MyLinkedList` class:

* `MyLinkedList()` Initializes the `MyLinkedList` object.
* `int get(int index)` Get the value of the `index^th` node in the linked list. If the index is invalid, return `-1`.
* `void addAtHead(int val)` Add a node of value `val` before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
* `void addAtTail(int val)` Append a node of value `val` as the last element of the linked list.
* `void addAtIndex(int index, int val)` Add a node of value `val` before the `index^th` node in the linked list. If `index` equals the length of the linked list, the node will be appended to the end of the linked list. If `index` is greater than the length, the node will not be inserted.
* `void deleteAtIndex(int index)` Delete the `index^th` node in the linked list, if the index is valid.  

Example 1:  
 
> Input:  
  \["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"\]  
  [[], [1], [3], [1, 2], [1], [1], [1]]  
  Output:  
  \[null, null, null, null, 2, null, 3\]  
  Explanation:  
  MyLinkedList myLinkedList = new MyLinkedList();  
  myLinkedList.addAtHead(1);  
  myLinkedList.addAtTail(3);  
  myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3  
  myLinkedList.get(1);              // return 2  
  myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3  
  myLinkedList.get(1);              // return 3  
  
  
Constraints:  
> 0 <= index, val <= 1000  
  Please do not use the built-in LinkedList library.  
  At most 2000 calls will be made to get, addAtHead, addAtTail,  addAtIndex and deleteAtIndex.

**Solution**  
* 解法一：
    按照正常的linkedlist思路设计，加一个size来判断index的合法性
* 解法二：  
    优化addAtHead，通过设计整个linkedlist有一个dummyHead，也就是一个指针指向整个linkedlist的开头。
* 解法三：
    在优化了addAtHead的基础上，将linkedlist设计成一个循环linkedlist，如此一来，可以将addAtTail从O(n)优化到O(1), 这种方法牺牲了一定的空间来减少时间复杂度


