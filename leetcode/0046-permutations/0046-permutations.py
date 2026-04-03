class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        hld = []
        vs = [False] * n
        def dfs(i):
            if i==n:
                res.append(hld.copy())
                return
            for j in range(n):
                if vs[j]: continue
                vs[j] = 1
                hld.append(nums[j])
                dfs(i+1)
                hld.pop()
                vs[j] = 0
        dfs(0)
        return res
            
        