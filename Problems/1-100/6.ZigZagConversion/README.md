## [6. ZigZag Conversion](https://leetcode-cn.com/problems/zigzag-conversion/)  

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

``` 
P   A   H   N
A P L S I I G
Y   I   R  
```
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:  
```string convert(string s, int numRows);```


Example 1:
>Input: s = "PAYPALISHIRING", numRows = 3  
Output: "PAHNAPLSIIGYIR"  

Example 2:
>Input: s = "PAYPALISHIRING", numRows = 4  
Output: "PINALSIGYAHRPI"  
Explanation:  
```
P     I    N  
A   L S  I G  
Y A   H R
P     I
```
Example 3:
>Input: s = "A", numRows = 1
Output: "A"

**Solution**
* 创建四个StringBuilder 表示每一行， go over 整个string， 用一个指针ind表示每一个循环当前char应该插入在第几行的stringbuilder后面。  
  当ind=0时，ind持续增加1 直至ind=numRows， 然后ind持续减少1，直至ind=0； repeat steps。  
  Time Complexity: O(n)