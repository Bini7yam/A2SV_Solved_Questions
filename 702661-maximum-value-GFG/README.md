# [Maximum value](https://www.geeksforgeeks.org/problems/maximum-value5946/1)
## Easy
Given an array arr[] of integres. Find the maximum value of arr[j] – arr[i] + arr[l] – arr[k], such that i &lt; j &lt; k &lt; l.Examples:
Input: arr[] = [1, 2, 3]
Output: -1
Explanation: arr.size() &lt; 4 so no such i,j,k,l is possible.

Input: arr[] = [4, 8, 9, 2, 20]
Output: 23
Explanation: Here i = 0, j = 2, k = 3, l = 4 so arr[j] – arr[i] + arr[l] – arr[k] = 9 – 4 + 20 – 2 = 23

Expected Time Complexity: O(n)Expected Auxiliary Space: O(n)
Constraints:1 ≤ arr.size() ≤ 1051 ≤ arr[i] ≤ 105