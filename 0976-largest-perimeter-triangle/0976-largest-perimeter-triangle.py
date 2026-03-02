class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        for i in range(2,n):
            a,b,c = nums[i-2], nums[i-1], nums[i]
            if a + b <= c: continue
            res = max(res, a + b + c)
        return res
        