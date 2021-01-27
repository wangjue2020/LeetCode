## [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)  
You are given an integer array nums sorted in ascending order (with distinct values), and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

 

Example 1:
>Input: nums = [4,5,6,7,0,1,2], target = 0  
Output: 4  

Example 2:
>Input: nums = [4,5,6,7,0,1,2], target = 3  
Output: -1  

Example 3:
>Input: nums = [1], target = 0  
Output: -1  

**Solution**
* 可以通过判断target是不是大于第0位数字，如果大于，则一定在array 前面递增部分，如果search到中间rotate的地方，就说明不存在，
    如果小于，则一定在array后面递增部分，可以直接从后往前search，如果search到了中间rotate的地方，则说明不存在  
    Time Complexity: O(N)  
    
* 利用二分法， 合理处理各种l 和r 指针的更新。  
    Time Complexity ： O(logn)
    