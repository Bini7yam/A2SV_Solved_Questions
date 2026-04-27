# [Count subsequences of type a^i, b^j, c^k](https://www.geeksforgeeks.org/problems/count-subsequences-of-type-ai-bj-ck4425/1)
## Medium
Given a string S, the task is to count number of subsequences of the form aibjck, where i &gt;= 1, j &gt;=1 and k &gt;= 1.

Note:&nbsp;
1.&nbsp;Two subsequences are considered different if the set of array indexes picked for the 2 subsequences are different.
2.&nbsp;&nbsp;For large test cases, the output value will be too large, return the answer MODULO 10^9+7

&nbsp;

Example 1:

Input:
S = "abbc"
Output: 3
Explanation: Subsequences are abc, abc and abbc.


Example 2:

Input:
S = "abcabc"
Output: 7
Explanation: Subsequences are abc, abc,
abbc, aabc abcc, abc and abc.


Your Task:
You don't need to read input or print anything. Your task is to complete the function&nbsp;fun()&nbsp;which takes the string S as input parameter and returns the number of subsequences which follows given condition.


Expected Time Complexity:&nbsp;O(Length of String).
Expected Auxiliary Space:&nbsp;O(1) .


Constraints:
1 &lt;= |S| &lt;= 105
