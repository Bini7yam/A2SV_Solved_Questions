class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4: return n-1
        dp = [0] * (n+5)
        dp[2]=2
        dp[3]=3
        for i in range(4,n+1):
            dp[i] = max(x * dp[i-x] for x in range(1,i-1))
        return dp[n]
    
        