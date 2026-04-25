class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        d = 3
        for i in range(1,n): d += d
        c = 0
        s = []
        r = ''
        def dfs():
            nonlocal c,r
            if len(s)==n:
                c += 1
                if c==k: r = ''.join(s)
                return
            rf = [i for i in 'abc' if i != s[-1]] if s else list('abc')
            for e in rf:
                s.append(e)
                dfs()
                if r: return
                s.pop()
        dfs()
        return r
