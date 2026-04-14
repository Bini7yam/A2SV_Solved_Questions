class Solution:
    def lastRemaining(self, n: int) -> int:
        l = 1
        r = n
        if r==1: return 1
        d = 1
        for i in range(30):
            if i&1: r -= d
            else: l += d
            if (r&d) ^ (l&d): 
                if i&1: l += d
                else: r -= d
            if l==r: return l
            d<<=1

        