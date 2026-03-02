class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def find(k):
            mp = {}
            l = c = res = 0
            n = len(nums)
            for i in range(n):
                x = nums[i]
                if x not in mp or not mp[x]:
                    mp[x] = 1
                    c += 1
                else: mp[x] += 1
                while c > k:
                    y = nums[l]
                    mp[y] -= 1
                    c -= not mp[y]
                    l += 1
                res += i - l + 1
            return res
        return find(k) - find(k-1)
        