class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0]*n for i in range(n)]
        pre = [0] * (n+1)
        for i in range(n): pre[i+1] = pre[i] + nums[i]
        for i in range(n): dp[i][i] = nums[i]
        for ln in range(2,n+1):
            for i in range(n):
                j = i + ln - 1
                if j >= n: break
                dpl = nums[i] + pre[j+1] - pre[i+1] - dp[i+1][j]
                dpr = nums[j] + pre[j] - pre[i] - dp[i][j-1]
                dp[i][j] = max(dpl, dpr)
        return 2 * dp[0][n-1] >= pre[n]
