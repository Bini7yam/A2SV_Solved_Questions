class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        dummy = []
        def dfs(i):
            if i==len(nums): 
                res.append(dummy.copy())
                return
            dummy.append(nums[i])
            dfs(i+1)
            dummy.pop()
            dfs(i+1)
        dfs(0)
        return res