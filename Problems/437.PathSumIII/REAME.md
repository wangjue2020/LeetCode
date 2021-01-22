## [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/)  
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:
```
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
```
**Solution（    效率不高，需要考虑新的方法）**
* 用recursion， 每次return 当前node到leaf之前所有可能的path的和。同时有一个class 范围的field `a` 记录path 的和等于sum的个数。  
    1. 如果当前node 是null， return empty arrayList
    1. 如果当前node 是leaf， check这个是不是等于sum，等于sum则，a++ 。  
    1. 如果不是node， 则recursion，   
        1. check这个node.val是不是等于sum，等于sum则，a++,  
        1. 将left child 和right child跑完return的list 里的和都加上当前node.val 并check是不是等于sum，及时a++， 再return新的list。
