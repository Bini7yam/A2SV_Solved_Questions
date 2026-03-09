class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {}
        mp[0] = 1
        cnt = res = 0
        for x in nums:
            cnt += x
            if cnt - k in mp: res += mp[cnt - k]
            if cnt in mp: mp[cnt]+=1
            else: mp[cnt]=1
        return res