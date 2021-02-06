## [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)  
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:  
Given tree s:
```
     3
    / \
   4   5
  / \
 1   2
 ```
Given tree t:
```
   4 
  / \
 1   2
 ```
Return true, because t has the same structure and node values with a subtree of s.
 

Example 2:  
Given tree s:
```
     3
    / \
   4   5
  / \
 1   2
    /
   0
   ```
Given tree t:
```
   4
  / \
 1   2
```
Return false.  

**Solution**
* BFS+Recursively  
用BFS浏览大的tree，一旦遇到val与小tree的root值相同的node，就比对这个node的subtree和小的tree是否一样  

* Preorder
将两个tree用preorder的方式return出preorder的顺序作为string输出，然后check大的tree的preorder string是否包含小的tree的preorder string，如果包含则说明是subtree。  
为了避免类似[12], [2] 出现"12"， "2"的情况，则在每一个node前面要加上一个标记，使得说明这个数字是一个整体， 同时也为了避免无法区分left child 还是right child，所以对于是null的我们要加上lnull, 或者rnull来表示并区分
