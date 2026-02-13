class Solution:
    def countNegatives(self, g: List[List[int]]) -> int:
        n,m=len(g),len(g[0])
        l = res = 0
        for i in range(n-1,-1,-1):
            while l < m and g[i][l] >= 0: l+=1
            if l==m: return res
            res += m - l
        return res
        