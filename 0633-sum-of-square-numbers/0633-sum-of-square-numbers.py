class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        while i*i <= c:
            d = c - i*i
            sd = floor(sqrt(d))
            if sd * sd == d: return True
            i += 1
        return False
        