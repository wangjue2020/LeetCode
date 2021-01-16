## [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)  
Given two sorted integer arrays `nums1` and `nums2`, merge `nums2` into `nums1` as one sorted array.

The number of elements initialized in `nums1` and `nums2` are m and n respectively. You may assume that `nums1` has enough space (size that is equal to `m + n`) to hold additional elements from `nums2`.

 

Example 1:
>Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3  
Output: [1,2,2,3,5,6]  

Example 2:
>Input: nums1 = [1], m = 1, nums2 = [], n = 0  
Output: [1]  

**Solution**
* 用两个指针分别指向两个array的有效部分的尾端，也就是nums1 和nums2 分别的最大值的地方，每次比对，选取较大的数字插入第三个指针所指向的地址，而第三个指针则是从nums1整个array尾端开始不断向前移位。
    Time Complexity: O(n)