class Solution:
    def longestBalanced(self, s: str) -> int:
        mx = 0
        n = len(s)
        def calc(a,b):
            nonlocal n
            mx = 0
            d = {}
            r = [0,0]
            d[str(r)] = -1
            for i in range(n):
                c = s[i]
                if c==a: r[0]+=1
                elif c==b: r[1]+=1
                else:
                    d.clear()
                    r = [0,0]
                    d[str(r)]=i
                if r[0] and r[1]: 
                    r[0]-=1
                    r[1]-=1
                key = str(r)
                if key in d: mx = max(mx, i-d[key])
                else: d[key] = i
            return mx
        r = 0
        ls = "*"
        a = [0,0,0]
        d={}
        d[str(a)]=-1
        for i in range(n):
            c = s[i]
            a[0] += c=='a'
            a[1] += c=='b'
            a[2] += c=='c'
            if a[0]*a[1]*a[2]:
                a[0]-=1
                a[1]-=1
                a[2]-=1
            key = str(a)
            if key in d: mx = max(mx, i-d[key])
            else: d[key] = i
            if c==ls:r+=1
            else:r=1
            ls=c
            mx = max(mx,r)
        mx = max(mx, calc('a','b'))
        mx = max(mx, calc('a','c'))
        mx = max(mx, calc('b','c'))
            
        return mx

