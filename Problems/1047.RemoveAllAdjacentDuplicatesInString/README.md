## [1047. Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)

Given a string `S` of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.  

Example 1:
>Input: "abbaca"  
Output: "ca"  
Explanation:   
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".  

**Solution**
* Use stack to store each letter, check whether the top of the stack is same as the one in current loop, if it is, then pop it, otherwise, push the current letter into stack.  
Time Complexity: O(n)