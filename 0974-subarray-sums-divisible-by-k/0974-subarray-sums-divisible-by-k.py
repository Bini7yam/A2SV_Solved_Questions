class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp = {0:1}
        rn = res = 0
        for num in nums:
            rn = (rn + num) % k
            if rn in mp: mp[rn]+=1
            else: mp[rn] = 1
            res += mp[rn]
        return res - len(nums)
        