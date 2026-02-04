class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        ls = -1
        res = []
        for x in nums:
            if x==ls:res.append(x)
            ls = x
        return res