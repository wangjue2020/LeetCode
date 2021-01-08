## [242. Valid Anagram](https://leetcode.com/problems/valid-anagram)   
Given two strings s and t , write a function to determine if t is an anagram of s.  

Example 1:  
> Input: s = "anagram", t = "nagaram"  
  Output: true
  
Example 2:  
> Input: s = "anagram", t = "nagaram"  
  Output: true  
  
  Note:  
  You may assume the string contains only lowercase alphabets.
  
**Solution**  
* HashMap  
    record the occurrence of each alphabet in first string, and compare to the second string.  
    Time Complexity: O(n)  
* HashTable  
    use HashTable instead of HashMap to reduce space complexity, use the index of array to identify different alphabets.  
    Time Complexity: O(n)  
    Space Complexity: O(1)