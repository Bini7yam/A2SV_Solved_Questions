class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        pre = [0] * (n+1)
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]: stack.pop()
            left[i] = stack[-1] + 1 if stack else 0
            stack.append(i)
            pre[i+1] = pre[i] + nums[i]
        stack = []
        res = 0
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]] >= nums[i]: stack.pop()
            right[i] = stack[-1] - 1 if stack else n-1
            l,r = left[i], right[i]
            res = max(res, (pre[r+1] - pre[l]) * nums[i])
            stack.append(i)
        mod = 1000000007
        return res % mod
        