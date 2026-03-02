class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        nums = [str(i) for i in nums]
        for i in range(n+3):
            for j in range(1,n):
                if nums[j] + nums[j-1] > nums[j-1] + nums[j]:
                    nums[j],nums[j-1] = nums[j-1],nums[j]
        s  = ''.join(nums)
        if s[0]=='0': s = '0'
        return s
        