## [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)  

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.  

Example 1:
>Input: digits = "23"  
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
>Input: digits = ""  
Output: []  

Example 3:
>Input: digits = "2"  
Output: ["a","b","c"]

**Solution**
* 用到了类似于BFS的解法把所有的可能性穷举出来。 
    Time Complexity: O(3^N * 4^M), N 表示代表三个字母的按键个数， M表示代表四个字母的按键字数  