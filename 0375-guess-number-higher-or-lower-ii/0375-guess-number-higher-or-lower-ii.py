class Solution:
    def getMoneyAmount(self, n: int) -> int:

        @cache
        def dp(l,r):
            if l > r: return 0
            if l==r:return 0
            if l+1==r:return l
            return min(max(dp(l,p-1), dp(p+1,r))+p for p in range(l+1,r))
       
        return dp(1,n)
        