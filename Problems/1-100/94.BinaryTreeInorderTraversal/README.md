## [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)  
Given the root of a binary tree, return the inorder traversal of its nodes' values.  

** Solution**
Inorder 是先go through left subtree 然后当前的node的val，然后go through right subtree
* Recursive
    ans = recursion result for left subtree + current val + recursion result for right subtree  
    Time Complexity: O(N)
    
* Iteration
    用iterative method 替代recursion， 思路类似  
    Time Complexity: O(N)  
    Space Complexity: O(n)