## [155. Min Stack](https://leetcode.com/problems/min-stack/)  

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

* push(x) -- Push element x onto stack.
* pop() -- Removes the element on top of the stack.
* top() -- Get the top element.
* getMin() -- Retrieve the minimum element in the stack.
 

Example 1:
>**Input**  
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]  
**Output**  
[null,null,null,null,-3,null,0,-2]  
**Explanation**  
MinStack minStack = new MinStack();  
minStack.push(-2);  
minStack.push(0);  
minStack.push(-3);  
minStack.getMin(); // return -3  
minStack.pop();  
minStack.top();    // return 0  
minStack.getMin(); // return -2  

**Solution**
* getMin() : loop the whole stack  
    Time Complexity: O(n)  
* user two stacks  
    一个栈存放全部的元素，push，pop都是正常操作这个正常栈。  
    另一个存放最小栈。 每次push，如果比最小栈的栈顶还小，我们就push进最小栈，否则不操作  
    每次pop的时候，我们都判断其是否和最小栈栈顶元素相同，如果相同，那么我们pop掉最小栈的栈顶元素即可  