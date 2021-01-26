## [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)  
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:
>Input: n = 3  
Output: ["((()))","(()())","(())()","()(())","()()()"]  

Example 2:
>Input: n = 1  
Output: ["()"]  

**Solution**
* BFS  
    用到BFS的方法，每次把增加一个长度的可能性加入到queue。
    Time Complexity: O(2^n)
