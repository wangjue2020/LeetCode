## [821. Shortest Distance to a Character](https://leetcode.com/problems/shortest-distance-to-a-character/)  

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:
>Input: S = "loveleetcode", C = 'e'  
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

**Solution**
* return 的array  `ans` 数字变化只有两种可能，一种是从指定character开始向右依次增大，和向左依次增大。
    可以将问题分为两个loop，第一次loop，我们从左到右寻找c，假设一开始c在非常小的index上，然后每loop一个index，将它与c的距离设置为index-pre， pre为上一次遇到的c的位置，如此一来，ans的数字顺序是从左至右，从大到小，直到0，再接着从大到小直到0。  
    第二次loop，我们从右至左寻找c，假设一开始c在非常大的index上，然后每loop一个index，将它与c的距离设置为pre-index， pre为上一次遇到的c的位置，如此一来， ans里在这个位置的数字为`min(之前的数字，和新的距离即pre-index)`  , 于是就可以得到从c开始向两头依次增大距离，得到最终的ans  
    Time Complexity: O(n)  
    