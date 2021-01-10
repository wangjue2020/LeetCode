## [203. Remove LinkedList Elements](https://leetcode.com/problems/remove-linked-list-elements/)
 

Remove all elements from a linked list of integers that have value val.  

Example 1:  
>Input:  1->2->6->3->4->5->6, val = 6  
 Output: 1->2->3->4->5

**Solution**  
* 解法一：
    go over 整个linkedlist,遇到需要删除的就进行删除，更新前一个node的next指针。需要对第一个node进行特殊处理，如果第一个node就需要删除的话。  
    Time complexity: O(n)   
    Space complexity: O(1)
* Dummy Node  
    对于第一个node就需要删除的情况进行优化，弄一个dummyNode，其next指向head， 这样就第一个node就需要删除的情况也可以归类到其他位置删除的情况。 
    Time complexity: O(n)   
    Space complexity: O(1)


