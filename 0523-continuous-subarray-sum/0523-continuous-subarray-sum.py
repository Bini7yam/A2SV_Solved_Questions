class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = set()
        pre = cnt = 0
        for x in nums:
            cnt = (cnt + x) % k
            if cnt in s: return True
            s.add(pre)
            pre = cnt
        return False