class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        sm = 0
        mp = {}
        for x in skill:
            sm += x
            if x in mp:mp[x]+=1
            else: mp[x]=1
        n = len(skill)//2
        if sm % n: return -1
        vd = sm//n
        st = set()
        vs = [False] * 2000
        res = 0
        for x in mp:
            if vs[x]: continue
            y = vd - x
            if y==x:
                if mp[x] & 1: return -1
                res += x * x * mp[x]//2
                continue
            vs[x] = vs[y] = True
            if y not in mp: return -1
            if mp[x] - mp[y]: return -1
            res += mp[x] * x * y
        return res
        