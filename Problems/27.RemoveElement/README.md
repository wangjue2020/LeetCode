## [27. Remove Element](https://leetcode.com/problems/remove-element/)
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Internally you can think of this:
```
// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

Example 1:
>Input: nums = [3,2,2,3], val = 3  
  Output: 2, nums = [2,2]  
  Explanation:   
  Your function should return length = 2, with the first two elements of nums being 2.  
  It doesn't matter what you leave beyond the returned length.  
   For example if you return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], your answer will be accepted.
  

Example 2:
> Input: nums = [0,1,2,2,3,0,4,2], val = 2  
 Output: 5, nums = [0,1,4,0,3]  
 Explanation:   
 Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.   
 Note that the order of those five elements can be arbitrary.   
 It doesn't matter what values are set beyond the returned length.


Constraints:

>0 <= nums.length <= 100  
 0 <= nums[i] <= 50  
 0 <= val <= 100

**Solution**  

* 暴力解法  

    go over 整个array，每一找到第i位置的元素与val相同时，就将后面所有元素nums[i] = nums[i+1], 向前移。之后在再继续从i开始重复之前的操作  
    
    Time complexity:O(n^2)     
    Space complexity: O(1)
    
* 双指针法
    一个指针A用于go over 整个array，另一个指针B记录下一个available的index。
    在循环过程中，如果遇到与val相同的元素，则指针B停在这里，等待下一个与val不相同的元素放在此位置，指针A继续指向下一个来进行判断。如果遇到与val不相同的元素，则将元素放在available index（即指针B所指向的地方），指针B++。  
      
    Time complexity:O(n)  
    Space complexity: O(1)
