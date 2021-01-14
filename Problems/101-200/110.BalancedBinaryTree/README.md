## [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)  

Given a binary tree, determine if it is height-balanced.

>For this problem, a height-balanced binary tree is defined as:  
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 Example 1:  
> Input: root = [3,9,20,null,null,15,7]  
 Output: true
 
 Example 2:  
 >Input: root = [1,2,2,3,3,null,null,4,4]  
 Output: false  

 Example 3: 
> Input: root = []  
 Output: true
 
 **Solution**
 * Divide and Conquer  
 在记算binary tree的height的同时进行比对是否当前处于balanced Tree， 如果不是，则直接返回结果