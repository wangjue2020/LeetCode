## [31. Next Permutation](https://leetcode.com/problems/next-permutation/)  
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:
>Input: nums = [1,2,3]  
Output: [1,3,2]  

Example 2:
>Input: nums = [3,2,1]  
Output: [1,2,3]  

Example 3:
>Input: nums = [1,1,5]  
Output: [1,5,1]  

Example 4:
>Input: nums = [1]  
Output: [1]  

**Solution**
* 规律： 从后往前找到第一个不是按照从后往前一次递增的数字的index i， 然后找到在i到length-1的位置中找到最小的比nums[i] 大的数字的index j, 将i和j位置的数字交换，然后再把从i+1到lenght-1，整个reverse  
    Time Complexity : O(n)