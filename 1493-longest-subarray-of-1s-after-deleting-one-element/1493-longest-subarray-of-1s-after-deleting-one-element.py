class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        c = 0
        n = len(nums)
        left = [0] * n
        right = [0] * n
        for i in range(n):
            left[i] = c
            if nums[i]: c+=1
            else: c=0
        c = res = 0
        for i in range(n-1,-1,-1):
            right[i] = c
            if nums[i]: c+=1
            else: c= 0
            res = max(res, left[i] + right[i])
        return res