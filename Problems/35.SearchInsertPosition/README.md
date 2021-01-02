## [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)
 

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

 

Example 1:
>Input: nums = [1,3,5,6],  
target = 5  
Output: 2

Example 2:
>Input: nums = [1,3,5,6]  
 target = 2  
 Output: 1
 
Example 3:
> Input: nums = [1,3,5,6]  
target = 7  
Output: 4

Constraints:

>1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4 
nums contains distinct values sorted in ascending order.  
-10^4 <= target <= 10^4

**Solution**  

* 暴力解法  
go over 整个array，直接查找  
Time complexity: O(n)   
Space complexity: O(1)

* 二分法
用left，right双指针来锁定array的查询范围，每次先查询从left到right的中间位置mid的大小，来判断target是在当前范围的前半部分还是后半部分，并更新left、right。  
可以用于已经按照一定规律sorted的array查询  
Time complexity:O(logn)  
Space complexity: O(1)
