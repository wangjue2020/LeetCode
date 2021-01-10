## [383. Ransom Note](https://leetcode.com/problems/ransom-note/)   
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.
Example 1:  
> Input: ransomNote = "a", magazine = "b"  
 Output: false
  
Example 2:  
> Input: ransomNote = "aa", magazine = "ab"  
  Output: false
  
Example 3:
> Input: ransomNote = "aa", magazine = "aab"  
Output: true

  
**Solution**  
some solution as  [242. Valid Anagram](../201-300/242.ValidAnagram)  
* HashMap  
    record the occurrence of each alphabet in first string, and compare to the second string.  
    Time Complexity: O(n)  
* HashTable  
    use HashTable instead of HashMap to reduce space complexity, use the index of array to identify different alphabets.  
    Time Complexity: O(n)  
    Space Complexity: O(1)