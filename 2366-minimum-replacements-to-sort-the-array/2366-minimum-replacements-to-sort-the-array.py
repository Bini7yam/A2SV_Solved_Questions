class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        mn = int(1e12)
        cnt = 0
        nums = nums[::-1]
        for x in nums:
            if x <= mn:
                mn = x
            else:
                bl = (x+mn-1)//mn
                cnt += bl - 1
                mn = x // bl
        return cnt
        