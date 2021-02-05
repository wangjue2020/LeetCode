## [589. N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)  
Given an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Follow up:

Recursive solution is trivial, could you do it iteratively?

**Solution**
* Recursively  
    Time Complexity: O(n)  
* Iteratively
    用stack来存储node，将每次pop出来的node的val加到list中，然后将node 的children以倒序的顺序push到stack中，最后list所得即preorder的list