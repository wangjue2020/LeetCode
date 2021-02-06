## [965. Univalued Binary Tree](https://leetcode.com/problems/univalued-binary-tree/)  
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.  

Example 1:  
>Input: [1,1,1,1,1,null,1]  
 Output: true  
 
Example 2:  
>Input: [2,2,2,5,2]  
 Output: false   
 
**Solution**  
*Recursively
用preorder的方式浏览整个tree，判断是否出现不一样的值  

* Iteratively  
用循环的方法实现BFS，来判断  
Time Complexity: O(n)  
Space Complexity: O(n)  
总体来说iteratively的方式比recursively的方式优点在于，一旦发现不一样，即刻就可以return，而recursive需要全部check完