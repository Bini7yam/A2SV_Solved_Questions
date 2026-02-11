class Solution:
    def findValidPair(self, s: str) -> str:
        def check(t):
            nonlocal s
            a,b=t[0],t[1]
            da,db=int(a),int(b)
            return a!=b and s.count(a) == da and s.count(b) == db
        n = len(s)
        for i in range(1,n):
            t = s[i-1:i+1]
            if check(t): return t
        return ''
