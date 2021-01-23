## [575. Distribute Candies](https://leetcode.com/problems/distribute-candies/)


Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor.

The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.

Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.

 

Example 1:
>Input: candyType = [1,1,2,2,3,3]  
Output: 3  
Explanation:  
Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.

Example 2:
>Input: candyType = [1,1,2,3]  
Output: 2  
Explanation:  
Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3], or [2,3], she still can only eat 2 different types.

Example 3:
>Input: candyType = [6,6,6,6]  
Output: 1  
Explanation:  
Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.

**Solution**
* 遍历整个数组，分两种情况， 用boy记录男孩分到的糖果数，girl记录女孩分到的糖果数  
    1. 女孩已经有当前糖果种类，男孩糖果数不到一半，则分给男孩； 男孩糖果数已经一般，则分给女孩。  
    1. 女孩没有当前糖果种类，女孩糖果数不到一般，则分给女孩； 女孩糖果数已经一般，则分给男孩。  
   Time Complexity: O(n)  
   Space Complexity: O(n)  
   
* 如果糖果种类大于n /2（糖果种类数为n），妹妹最多可以获得的糖果种类应该是n / 2(因为妹妹只有n / 2个糖).  
  糖果种类数小于n / 2, 妹妹能够得到的糖果种类可以是糖果的种类数（糖果种类本身就这么多）.  
     Time Complexity: O(n)  
     Space Complexity: O(n) 