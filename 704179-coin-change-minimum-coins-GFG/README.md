# [Coin Change (Minimum Coins)](https://www.geeksforgeeks.org/problems/number-of-coins1824/1)
## Medium
You are given an array coins[], where each element represents a coin of a different denomination, and a target value sum. You have an unlimited supply of each coin type {coins1, coins2, ..., coinsm}. 
Your task is to determine the minimum number of coins needed to obtain the target sum. If it is not possible to form the sum using the given coins, return -1.
Examples:
Input:&nbsp;coins[] = [25, 10, 5], sum = 30Output:&nbsp;2Explanation:&nbsp;Minimum 2 coins needed, 25 and 5 &nbsp;
Input:&nbsp;coins[] = [9, 6, 5, 1], sum = 19Output:&nbsp;3Explanation:&nbsp;19 = 9 + 9 + 1
Input:&nbsp;coins[] = [5, 1], sum = 0Output:&nbsp;0Explanation:&nbsp;For 0 sum, we do not need a coin
Input:&nbsp;coins[] = [4, 6, 2], sum = 5Output:&nbsp;-1Explanation:&nbsp;Not possible to make the given sum.
&nbsp;
Constraints:1 ≤ sum * coins.size() ≤ 106
0 &lt;= sum &lt;= 104
1 &lt;= coins[i] &lt;= 104
1 &lt;= coins.size() &lt;= 103