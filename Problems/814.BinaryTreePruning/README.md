## [814. Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/)  
We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)  

把不含有1的节点的子树全部删除。

Example  1:  
>Input: [1,null,0,0,1]  
 Output: [1,null,0,null,1]  
 Explanation:   
 Only the red nodes satisfy the property "every subtree not containing a 1".
 The diagram on the right represents the answer.
 
Example 2:  
>Input: [1,0,1,0,0,0,1]  
Output: [1,null,1,null,1]  

Example 3:  
>Input: [1,1,0,1,1,0,1,0]  
Output: [1,1,0,1,1,null,1]  

**Solution**
*Recursively  
用recursion走到tree的最底层，一层一层往上判断是否应该删除当前node的子树
1. base case： 
    > node 为 null  ===》return true；  
    node为leaf ====》 如果node的val是1，return true，否则false；  
1. recursion:
    check left subtree 和 right subtree 里面是否存在1  
    1. left subtree 和 right substree 都存在1， 则return true，表示不能被删除  
    2. left subtree 和right subtree中有一个存在1， 有一个不存在，则将不存在的那一边指向null，并且查看另一边subtree是因为null才return true，还是因为存在1才return true.  
        如果是因为null，return需要判断当前node的value是不是1，是则return true， 不是则return false； 
        如果subtree不是因为null return的true，则说明是真的存在1，那么当前node也只能return true，因为不能被删除。  
    3. left subtree 和 right subtree 中都不存在1， 则将当前node的left，和right都指向null，并且判断当前node的value是不是1，是1 则return true， 否则false；  
    
整个recursion结束之后，还需要判断到了root的时候root 的boolean是true还是false，如果是false，则整个树都不存在1，整个包括root都需要被删除，直接return null。 如果是true，则直接return root，此时的root已经是修改过的了

Time Complexity： O(n)