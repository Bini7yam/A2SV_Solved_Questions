class Solution:
    def integerBreak(self, n: int) -> int:
        if n is 2: return 1
        if n is 3: return 2
        if n is 4: return 4
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n
        