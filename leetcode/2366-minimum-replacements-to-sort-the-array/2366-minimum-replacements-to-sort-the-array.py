class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        mn = int(1e12)
        cnt = 0
        n = len(nums)
        for i in range(n-1,-1,-1):
            x = nums[i]
            if x <= mn:mn = x
            else:
                bl = (x+mn-1)//mn
                cnt += bl - 1
                mn = x // bl
        return cnt
        