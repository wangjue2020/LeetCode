## [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)  
Given a string s, return the longest palindromic substring in s.

 

Example 1:
>Input: s = "babad"  
Output: "bab"  
Note: "aba" is also a valid answer.

Example 2:
>Input: s = "cbbd"  
Output: "bb"  

Example 3:
>Input: s = "a"  
Output: "a"  

Example 4:
>Input: s = "ac"  
Output: "a"  

**Solution**
* We define P(i,j) as following:
  
  P(i,j) = true if the substring Si ... Sj is a palindrome, otherwise false.  
  
  Therefore,
  P(i,j)=(P(i+1,j−1) and Si ==Sj)  
  
  The base cases are:
  P(i,i)=true  
  P(i, i+1) = ( Si == S_i+1 )  
  This yields a straight forward DP solution, which we first initialize the one and two letters palindromes, and work our way up finding all three letters palindromes, and so on...  
  在此基础上可以对于一开始P(i,i) expend, 将i--， j++ 直到Si...Sj不再palindromic， 也将P(i,i+1) extend 得到从P(i,i) ，P(i,i+1) 延伸得到的最大的palindrome string， 然后每一个i 都可以做extend，期间不断更新最长的palindrome string。  
  Time Complexity : O(N^2)