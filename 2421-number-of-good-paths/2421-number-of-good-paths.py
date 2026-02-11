class Solution:
    def numberOfGoodPaths(self, v: List[int], e: List[List[int]]) -> int:
        n = len(v)
        N = int(1e5 + 15)
        adj = [[] for i in range(n)]
        res= n
        for d in e:
            x,y = d
            adj[x].append(y)
            adj[y].append(x)
            res += v[x] == v[y]
        p = [-1]*n
        on = [False] * n
        ind = [[] for i in range(N)]
        for i in range(n):
            ind[v[i]].append(i)
        def find(x):
            if p[x]==x: return x
            y = find(p[x])
            p[x] = y
            return y
        def join(x,y):
            px,py=find(x),find(y)
            if px==py:return
            p[px] = py
        for lst in ind:
            if not lst:continue
            cnt = {}
            for x in lst:
                for y in adj[x]:
                    if not on[y]:continue
                    rep = find(y)
                    if rep not in cnt:cnt[rep]=0
                    res += cnt[rep]
                    cnt[rep] += 1
            for x in lst:
                p[x] = x
                on[x] = 1
                for y in adj[x]:
                    if not on[y]:continue
                    join(x,y)
        return res

        