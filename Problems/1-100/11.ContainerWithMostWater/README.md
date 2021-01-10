## [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
 

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.  

Example 1:  
>Input: height = [1,8,6,2,5,4,8,3,7]  
 Output: 49  
 Explanation:  
 The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
>Input: height = [1,1]  
 Output: 1
 
Example 3:  
> Input: height = [4,3,2,1,4]  
  Output: 16  
  
Constraints:

>n = height.length  
 2 <= n <= 3 * 10^4  
 0 <= height[i] <= 3 * 10^4  

**Solution**  
* 暴力解法 
 
    两个for loop 把每一种组合计算一遍  
    Time complexity: O(n^2)   
    Space complexity: O(1)
* double pointer
    用两个指针指向一头一尾，每次移动所对应的vertical line较短的一个指针，来获取新的possible container。  
    移动较短而不是较长的哪个指针是因为，如果移动的是较长的指针，而这跟较长的线是当前指针指向过的所有线中最长的一根，如果移动这根线所对应的指针，那么一定会得到一个小于或等于之前面积的container。  
    比如如果l指向的长度为a， r指向的长度为b，而a<b, l和r之间相隔width宽，area=a\*width 则：    
    1. 如果移动r， 并指向新的长度为c： 如果c>b, 则新的area=a*(width-1); 如果c<b, 则新的area=c*(width-1)；  
    1. 如果移动l，并指向新的长度c: 如果c>a, 则新的area=min(c,b)\*(width-1); 如果c<a, 则新的area=c\*(width-1);  
    
   所以case 1 的area一定会减小，case 2 的area可能减小，可能增大。 
     
   Time complexity: O(n)   
   Space complexity: O(1)


