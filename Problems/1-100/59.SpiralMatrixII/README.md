## [59. Spriral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/)
 

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

Example 1:  
![example result ](spiraln.jpg)  
>Input: n = 3  
 Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
>Input: n = 1  
 Output: [[1]]
 
Constraints:

>1 <= n <= 20  

**Solution**  
* for loop 1 to n^2, 每次在相应位置插入数字。用r 表示第几行，c表示第几列。  
    判断位置时，首先判断当前index上是否为0或者index是否合法， 为0则是当前位置可以插入数字， 不为零或者outOfIndex则说明螺旋方向需要改变，一共有四个方向，向右移，向下移，向左移，和向上移，以此循环。
    每次成功插入数字之后或者是螺旋方向改变之后都需更新到新的且符合条件的r、c  
    Time complexity: O(n^2)   
    Space complexity: O(1)


