## [108. Convert Sorted Array To Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)  

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:
```
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
```

**Solution**
* Create another method to build BST with parameters ( array nums, int start_ind, int end_ind ), start_ind is the start index of array, and end_ind is the end index of array, we only consider the nums[start_ind : end_ind] part.  
    every time find the number in the middle of array as the root of current subtree, and then do the recursion using left part array and right part array to build left subtree and right subtree.  
    Time Complexity: O(n)
