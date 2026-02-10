class Solution:
    def isHappy(self, n: int) -> bool:
        def cng(n):
            return sum(int(d)**2 for d in str(n))
        s = set()
        while n-1:
            if n in s: return False
            s.add(n)
            n = cng(n)
        return True
        