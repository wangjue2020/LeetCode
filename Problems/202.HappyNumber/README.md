## [202. Happy Number](https://leetcode.com/problems/happy-number/)  
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.  
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.  
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.   

Example 1:  
> Input: n = 19  
  Output: true  
  Explanation:  
  1^2 + 9^2 = 82  
  8^2 + 2^2 = 68  
  6^2 + 8^2 = 100  
  1^2 + 0^2 + 0^2 = 1  
  
Example 2:  
> Input: n = 2  
  Output: false  
  
**Solution**
  * HashSet
  since the problem description says do the designed summation until get 1, if it loops endlessly in a cycle then return false.  
  to avoid the endless while loop, we can use HashSet to record each result we obtain, if we get the same result again, which means it will be a infinite loop.  
  