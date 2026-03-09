class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mi=cur=0;ma=nums[0]
        for i in range(len(nums)):
            mi=min(mi,cur)
            cur+=nums[i]
            ma=max(ma,cur-mi)
        return ma 
        