## [198. House Robber](https://leetcode.com/problems/house-robber/)  
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:
>Input: nums = [1,2,3,1]  
Output: 4  
Explanation:  
Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:
>Input: nums = [2,7,9,3,1]  
Output: 12  
Explanation: 
 Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

**Solution**
* DP 
    对于第i户， 因为每偷一户， 另据都不可以再偷，所以如果偷第i户的话，上一户可能是第i-2，也有可能是第i-3， 所以记录对于如果从第一户到第i户可收获的最大利益 即 max(nums[i]+ profit[i-2], nums[i]+profit[i-3]);  
    为什么不用再考虑i-3前面的每一户，是因为，如果考虑i-4的话，从i-4 到i， 一共有 i-4, i-3, i-2, i-1， i， 那么如果从i-4直接到i，中间其实还可以偷第i-2户，所以为了利益最大化，只有可能是从i-3， 或这i-2到达第i户  
    Time Complexity: O(n)