## [1302. Deepest Leaves Sum](https://leetcode.com/problems/deepest-leaves-sum/)  
Given a binary tree, return the sum of values of its deepest leaves.  

Example 1: 
>Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]  
 Output: 15  
 
**Solution** 
* BFS  
    计算每一层的leaves和，每到下一层更新，直到最后一层，即答案  
    Time Complexity: O(n)