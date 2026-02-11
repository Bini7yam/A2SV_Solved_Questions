class Solution:
    def findCommonResponse(self, rs: List[List[str]]) -> str:
        d = {}
        mx = 0
        for r in rs:
            for s in set(r):
                if s in d: d[s]+=1
                else: d[s]=1
                mx = max(mx,d[s])
        res = ""
        for s in d.keys():
            if d[s]==mx:
                if not res or s < res:
                    res = s
        return res