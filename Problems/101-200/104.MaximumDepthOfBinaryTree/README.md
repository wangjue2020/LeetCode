##[104 Maximum Depth Of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.  


Example:
![temp-tree](./tmp-tree.jpg)  
>Input: root = [3,9,20,null,null,15,7]  
Output: 3  

Example 2:
>Input: root = [1,null,2]  
Output: 2  

Example 3:
>Input: root = []  
Output: 0  

Example 4:
>Input: root = [0]  
Output: 1  

**Solution**  
* BFS
 Use Breadth first search to go through the whole tree to compute the depth of binary tree  
 Time Complexity: O(n), n is the number of TreeNode  

* Divide and Conquer  
    Use Divide and Conquer to do recursion to go through the whole tree. 
