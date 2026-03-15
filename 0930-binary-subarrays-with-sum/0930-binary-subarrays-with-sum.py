class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        mp  = {}
        cnt = res = 0
        mp[0] = 1
        for num in nums:
            cnt += num
            if (cnt - goal) in mp: res += mp[cnt - goal]
            if cnt in mp: mp[cnt] += 1
            else: mp[cnt] = 1
        return res
        