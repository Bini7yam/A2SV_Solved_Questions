class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def score(l,r):
            if l == r: return nums[l]
            return sum(nums[l:r+1]) - min( score(l+1, r), score(l,r-1))
        n = len(nums)
        return 2*score(0,n-1) >= sum(nums)

        