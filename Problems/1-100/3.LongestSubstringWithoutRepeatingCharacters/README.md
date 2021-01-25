## [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)  
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:
>Input: s = "abcabcbb"  
Output: 3  
Explanation: The answer is "abc", with the length of 3.

Example 2:
>Input: s = "bbbbb"  
Output: 1  
Explanation: The answer is "b", with the length of 1.

Example 3:
>Input: s = "pwwkew"  
Output: 3  
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
>Input: s = ""  
Output: 0  

**Solution**
* 如果当前遍历到的字符从未出现过，那么直接扩大右边界；  
  如果当前遍历到的字符出现过，则缩小窗口（左边索引向右移动移动到字符出现的index的下一位），然后继续观察当前遍历到的字符；
  重复（1）（2），直到窗口内无重复元素；  
  维护一个全局最大窗口 res，每次用出现过的窗口大小来更新结果 res，最后返回 res 获取结果;
  最后返回 res 即可;  
  Time Complexity: O(n)  