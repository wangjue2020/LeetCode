## [590. N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/)  
Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).  

**Solution**  
* Recursively  
    Time Complexity: O(n)  

* Iteratively  
    用stack存储，每次取出并将val存到list中，然后把取出的node的children全部push到stack中。
    最终list里的顺序就是postorder 反过来的顺序，将顺序反过来即可。  