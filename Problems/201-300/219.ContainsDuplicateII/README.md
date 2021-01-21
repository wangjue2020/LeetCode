## [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)  
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
>Input: nums = [1,2,3,1], k = 3  
Output: true  

Example 2:
>Input: nums = [1,0,1,1], k = 1  
Output: true  

Example 3:
>Input: nums = [1,2,3,1,2,3], k = 2  
Output: false  

**Solution**
* Brute Force   
    Time Complexity: O(n^2)

* HashMap  
    map里面记录了每个数字上一次出现的index
    每次通过map检查当前数字是否出现过，如果没有出现过或者是上一次的出现位置index 和当前位置相差大于k，则将当前数字在map里的index 记录更新成当前的index， 因为之前的index是不可能在相差k以内的位置找到duplicates。
    如果当前数字出现过，且index和当前index相差在k以内，则return true；  
    Time Complexity: O(n)