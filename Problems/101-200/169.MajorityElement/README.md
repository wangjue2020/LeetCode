## [169.Majority Element](https://leetcode.com/problems/majority-element/)  
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:
>Input: nums = [3,2,3]  
Output: 3  

Example 2:
>Input: nums = [2,2,1,1,1,2,2]  
Output: 2  

**Solution**
* Sorting
    sort之后，占大多数的majority一定是在array中的中间位置，所以直接return中间length/2 的index的数值就好  
    Time Complexity: O(nlogn)  
* Boyer-Moore Voting Algorithm 
    类似于计票方法，占大多数majority的出现频率抵消掉其他小部分的数字之外是有余，所以每次遇到和当前majority相同的，count加一，否则减一，如果count到了0，说明目前这个majority并不是当前的大多数，换下一个位置的数字做majority即可  
    Time Complexity : O(n)