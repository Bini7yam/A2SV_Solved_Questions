class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        f = [0] * n
        for v in requests:
            l,r = v
            f[l] += 1
            if r+1 < n: f[r+1] -= 1
        
        for i in range(1,n): f[i] += f[i-1]
        print(f)

        nums.sort()
        f.sort()
        res = 0
        mod = int(1e9 + 7)
        for i in range(n):
            res += f[i] * nums[i] % mod
            res %= mod
        return res
            
        