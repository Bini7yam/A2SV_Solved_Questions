class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sm = 0
        for x in nums: sm += x
        n = len(nums)
        return n * (n+1) // 2 - sm
        
