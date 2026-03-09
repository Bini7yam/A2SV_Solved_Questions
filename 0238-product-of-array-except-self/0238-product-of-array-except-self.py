class Solution:
    def productExceptSelf(self, a: List[int]) -> List[int]:
        n = len(a)
        pre = [1]*(n+1)
        for i in range(n):
            pre[i+1] = pre[i] * a[i]
        suf = [1]*(n+1)
        for i in range(n-1,-1,-1):
            suf[i] = suf[i+1] * a[i]
        res = [0]*n
        for i in range(n):
            res[i] = pre[i] * suf[i+1]
        return res
        