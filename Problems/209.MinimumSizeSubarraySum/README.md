## [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:
>Input: s = 7, nums = [2,3,1,2,4,3]  
 Output: 2  
 Explanation:  
 the subarray [4,3] has the minimal length under the problem constraint.

Follow up:

If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

**Solution**  

* 暴力解法  

    两个for loop不断寻找每一种可能的subarray，从而获得length最小的且满足条件的subarray  
    Time complexity:O(n^2)     
    Space complexity: O(1)
    
* 滑动窗口法  
    两个指针，指针A指向窗口最左端，指针B指向窗口最右端， 整个窗口代表一个subarray。
    每当当前窗口的和小于s时，指针B右移一位，扩大窗口，如果当前窗口的和大于或等于s时，指针A右移一位，缩小窗口，以尝试是否可以缩小窗口且同时满足条件。每次符合条件的subarray，记录当前最小的subarray长度
    直到指针A或者指针B已经移到了array末端，则停止滑动，return 满足条件的最小窗口长度  
      
    Time complexity:O(n)  
    Space complexity: O(1)
