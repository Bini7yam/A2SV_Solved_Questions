class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2
        inf = 100000000
        dp = [inf] * (n+1)
        dp[0] = 0
        for i in range(n+n):
            a,b = costs[i]
            ndp = [inf] * (n+1)
            ndp[0] = dp[0] + b
            for j in range(1,n+1):
                ndp[j] = min(dp[j]+b,dp[j-1]+a)
            dp = ndp
        return dp[n]