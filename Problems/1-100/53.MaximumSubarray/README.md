## [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)  

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

 

Example 1:
>Input: nums = [-2,1,-3,4,-1,2,1,-5,4]  
Output: 6  
Explanation:   
[4,-1,2,1] has the largest sum = 6.  

Example 2:
>Input: nums = [1]  
Output: 1  

Example 3:
>Input: nums = [0]  
Output: 0  

Example 4:
>Input: nums = [-1]  
Output: -1  

Example 5:
>Input: nums = [-100000]  
Output: -100000  

**Solution**  
* Dynamic Programming  
    use DP to compute the maximum sum of subarray  from the index 0 to current index. update the maximum sum as well. 
    `nums[i] = Integer.max(nums[i], nums[i]+nums[i-1]);`   
 
    Time Complexity: O(N)
 