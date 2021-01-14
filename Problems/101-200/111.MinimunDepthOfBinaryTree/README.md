## [111. Minimum Depth Of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)  

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:  
![temp-tree](./tmp-tree.jpg)  
>Input: root = [3,9,20,null,null,15,7]  
Output: 2  

Example 2:
>Input: root = [2,null,3,null,4,null,5,null,6]  
Output: 5  

**Solution**  
* Divide and Conquer  
    divide into left subtree and right subtree and the do recursion.
    combine the result from left subtree and right subtree to get final answer.  
 
* BFS  
    go through the tree using Breadth First Search, once get a node who does not have left child nor right child, then return the current depth directly.  
    this method works better than divide and conquer. 
    
    Time Complexity: O(n)