##[541.Reverse String II](https://leetcode.com/problems/reverse-string-ii/)
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example:  
>Input: s = "abcdefg", k = 2  
Output: "bacdfeg"

**Solution**
* For every 2k element, do string reverse for first k elements. 
    Time Complexity: O(n)