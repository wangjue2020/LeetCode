## [1325. Delete Leaves With a Given Value](https://leetcode.com/problems/delete-leaves-with-a-given-value/)  
Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if it's parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you can't).  

Example 1:  
>Input: root = [1,2,3,2,null,2,4], target = 2  
 Output: [1,null,3,null,4]  
 Explanation:  
 Leaf nodes in green with value (target = 2) are removed (Picture in left). 
 After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).  
 
Example 2:  
>Input: root = [1,3,3,3,2], target = 3  
Output: [1,3,null,null,2]  

Example 3:  
>Input: root = [1,2,null,2,null,2], target = 2  
 Output: [1]  
 Explanation:  
 Leaf nodes in green with value (target = 2) are removed at each step.

Example 4:
> Input: root = [1,1,1], target = 1  
 Output: []  
 
Example 5:
> Input: root = [1,2,3], target = 1  
 Output: [1,2,3]  
 
**Solution**
* Recursively  
用recursion的方式从最底层往上一层层check， 这样可以解决当child node都是target被删除了之后，node本身也会成为一个target leaf的可能的问题  
每次return当前node是否应该被删除，如果是target leaf则return true，否则false。如此一来等到了当前node的parent的时候，他会进行check，并删除return true的child node。  
    1. base case：  
        当node 是null时，return true。  
        当node 是leaf时， 如果node的value 是target则return true，否则false。  
    1. recursion：  
        计算left child 和right child是否是target leaf。  
        如果左边和右边都是target leaf，则将node.left 和 node.right 都指向null，然后并check 自己本身是否构成一个新的target leaf 来return boolean。  
        如果左边和右边有一个是target leaf，则将对应那边指向null，并return false。  
        如果两边都不是target leaf， 则return false。 
        
    Time Complexity: O(n)  