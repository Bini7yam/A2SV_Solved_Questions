class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(2,n):
            j = i - 2
            if nums[j]: continue
            nums[j] = 1
            nums[j+1] ^= 1
            nums[i] ^= 1
            res += 1
        return res if nums[-1] and nums[-2] else -1