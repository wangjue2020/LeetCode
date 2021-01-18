## [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)  
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
>Input: "A man, a plan, a canal: Panama"  
Output: true  

Example 2:
>Input: "race a car"  
Output: false  

**Solution**  
* 用双指针指向一头一尾逐个比对， 对于特殊符号进行跳过操作  
 Time Complexity: O(n)  