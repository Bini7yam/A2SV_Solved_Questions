class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        mn = 0
        rn = 0
        for num in nums:
            rn += num
            mn = min(mn, rn)
        return 1 - min(0,mn)
        