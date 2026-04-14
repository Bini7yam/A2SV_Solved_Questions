class Solution:
    def lastRemaining(self, n: int) -> int:
        l = 1
        r = n
        if r==1: return 1
        for i in range(30):
            if i&1: r -= 1<<i
            else: l += 1<<i
            if (r&1<<i) ^ (l&1<<i): 
                if i&1: l += 1<<i
                else: r -= 1<<i
            if l==r: return l

        