## [15. 3 Sum](https://leetcode.com/problems/3sum/)

Given an array `nums` of n integers, are there elements a, b, c in `nums` such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:
>Input: nums = [-1,0,1,2,-1,-4]  
Output: [[-1,-1,2],[-1,0,1]]  


Example 2:
>Input: nums = []  
Output: []  

Example 3:
>Input: nums = [0]  
Output: []

**Solution**
* Double pointer
    1. sort array
    1. go over the array, for each element `a` at index `i`, try to find the `b` at index `l` and `c` at index `r` from index `i+1` to the index `nums.length-1` 
    1. record the suitable a, b c into a hashSet as a list.
    1. if `a+b+c` < 0, `l++`; if `a+b+c` > 0, `r--`; Otherwise `l++` and `r--`, to avoid duplicate cases. 
    1. for the outer for loop, skip the element, if it is equal to the previous one.   
 
    Time Complexity: O(nlogn) for sort, totally O(n^2)
