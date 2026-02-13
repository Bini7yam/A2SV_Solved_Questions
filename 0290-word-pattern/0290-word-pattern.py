class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        d = {}
        r = {}
        s = s.split()
        n = len(s)
        if n != len(p):return False
        for i in range(n):
            if p[i] in d:
                if d[p[i]] != s[i]: return False
            if s[i] in r:
                if r[s[i]] != p[i]: return False
            d[p[i]]=s[i]
            r[s[i]]=p[i]
        return True
        