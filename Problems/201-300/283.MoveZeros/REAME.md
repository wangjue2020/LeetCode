## [283. Move Zeros](https://leetcode.com/problems/move-zeroes/)  
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
>Input: [0,1,0,3,12]  
Output: [1,3,12,0,0] 

**Solution**  
* Similar idea as [26. Remove Duplicates From Array](../../1-100/26.RemoveDuplicatesFromArray)  
    用两个指针，一个用来go through array，一个用来表示next available index。
    Time Complexity : O(n)  
    Space Complexity : O(1)  