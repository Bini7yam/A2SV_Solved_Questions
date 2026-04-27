# [Skip the work](https://www.geeksforgeeks.org/problems/skip-the-work5752/1)
## Medium
Given an array A[ ] denoting the time taken to complete N tasks, determine the minimum amount of time required to finish the tasks considering that you can skip any task, but&nbsp;skipping two consecutive tasks is forbidden.
&nbsp;

Example 1:

Input:
N = 2
A[] ={10,20}
Output: 10
Explanation: we can take time of
10 units and skip 20 units time.



â€‹Example 2:

Input:
N = 4
A[] = {10,5,7,10}
Output: 12
Explanation: we can skip both the
tens and pick 5 and 7 only.


&nbsp;

Your Task:
You don't need to read input or print anything. Your task is to complete the function&nbsp;minAmount()&nbsp;which accepts array A[]&nbsp;and its size&nbsp;N&nbsp;as input parameter and returns&nbsp;minimum amount of time required to finish the tasks.


Expected Time Complexity:&nbsp;O(N)
Expected Auxiliary Space:&nbsp;O(1)


Constraints:
1 &lt;= N&nbsp;&lt;= 106

&nbsp;
