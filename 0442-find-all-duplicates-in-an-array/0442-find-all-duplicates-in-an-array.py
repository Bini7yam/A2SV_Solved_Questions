class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for x in nums:
            y = abs(x)
            if nums[y-1]<0:res.append(y)
            else: nums[y-1]*=-1
        return res