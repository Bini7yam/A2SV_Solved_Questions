class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 'xy'
        yx = 'yx'
        n = len(s1)
        cxy = cyx = 0
        for i in range(n):
            t = s1[i] + s2[i]
            cxy += t == xy
            cyx += t == yx
        res = cxy//2 + cyx//2
        cxy &= 1
        cyx &= 1
        if cxy ^ cyx: return -1
        return res + cxy + cyx

        