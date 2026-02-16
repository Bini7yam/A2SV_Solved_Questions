# [Nth Catalan Number](https://www.geeksforgeeks.org/problems/nth-catalan-number0817/1)
## Medium
Given a number n. The task is to find the nth catalan number.The first few Catalan numbers for n = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …Catalan Number&nbsp;for n is equal to the number of expressions containing n pairs of parenthesis that are correctly matched, i.e., for each of the n(' there exist n ')' on there right and vice versa.Note: Positions start from 0 as shown above.
Examples:
Input: n = 3
Output: 5Explanation: Possible expressions are, ((())), (()()), ()(()), (())(), ()()()
Input: n = 4
Output: 14Explantions: There are total 14 valid combinations which can be formed using 4 parenthesis.
Constraints:1 &lt;= n &lt;= 19