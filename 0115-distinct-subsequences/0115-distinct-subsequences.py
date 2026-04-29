class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ns,nt=len(s),len(t)
        #dp = [x] * nt
        dp = [0] * (nt+1)
        dp[0] = 1
        for c in s:
            for i in range(nt,0,-1):
                dp[i] = dp[i] + (t[i-1]==c) * dp[i-1]
        return dp[nt]
        