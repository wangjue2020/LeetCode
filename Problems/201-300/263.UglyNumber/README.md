## [263. Ugly Number](https://leetcode.com/problems/ugly-number/)  
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:
>Input: 6  
Output: true  
Explanation: 6 = 2 × 3

Example 2:
>Input: 8  
Output: true  
Explanation: 8 = 2 × 2 × 2

Example 3:
>Input: 14  
Output: false   
Explanation: 14 is not ugly since it includes another prime factor 7.  

**Solution**
* 只要能整出2，就去掉所有2的factor， 重复步骤去除所有3的factor，和5的factor，最后如果等于1则说明这个数字的factor只有2，3，5， 否则还存在其他的factor  
    Time Complexity: O(logn)