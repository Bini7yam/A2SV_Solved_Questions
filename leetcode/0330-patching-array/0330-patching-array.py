class Solution:
    def minPatches(self, nums: List[int], x: int) -> int:
        n = len(nums)
        r = i = p = res = 0
        while r < x:
            if i-n and nums[i] == p:
                r += p
                i += 1
                continue
            if p > r:
                r += p
                res += 1
                p += 1
                continue
            if i < n: p += 1
            else: p = r + 1
        return res
        