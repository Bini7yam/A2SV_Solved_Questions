class Solution:
    def rob(self, arr: List[int]) -> int:
        n = len(arr)
        if n<4: return max(arr)
        def solve(nums):
            n = len(nums)
            dp = [0]*(n+5)
            dp[0] = nums[0]
            if n==1: return dp[0]
            dp[1] = max(nums[0],nums[1])
            if n==2: return dp[1]
            dp[2] = max(nums[0]+nums[2],nums[1])
            if n==3: return dp[2]
            for i in range(3,n):
                dp[i] = nums[i] + max(dp[i-2], dp[i-3])
            return max(dp[n-2],dp[n-1])
        return max(solve(arr[1:]), solve(arr[:-1]))

        