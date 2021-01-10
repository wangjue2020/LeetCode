## [454. 4 Sum II](https://leetcode.com/problems/4sum-ii/)
Given four lists A, B, C, D of integer values, compute how many tuples `(i, j, k, l)` there are such that `A[i] + B[j] + C[k] + D[l]` is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
Example 1:  
> Input:  
A = [ 1, 2]  
B = [-2,-1]  
C = [-1, 2]  
D = [ 0, 2]  
Output:  2
Explanation:  
The two tuples are:  
(0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0  
(1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

**Solution**  
* HashMap  
use a HashMap recording the sum and occurrence of the sum for A, B.(sum is A[i]+B[j] for any i or j).  
repeat the step to get second HashMap for C, D.   
like the way to check [1.two sum](../1-100/1.TwoSum) to check whether there exists any pair of sums whose sum is 0.  
Time Complexity: O(n^2)