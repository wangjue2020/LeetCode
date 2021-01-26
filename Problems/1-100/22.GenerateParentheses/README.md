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
    Time Complexity:  O((4^n)/(sqrt(n)))
* DFS  
    Instead of adding '(' or ')' every time, let's only add them when we know it will remain a valid sequence. We can do this by keeping track of the number of opening and closing brackets we have placed so far.
    
    We can start an opening bracket if we still have one (of n) left to place. And we can start a closing bracket if it would not exceed the number of opening brackets.
    Time Complexity: O((4^n)/(sqrt(n)))