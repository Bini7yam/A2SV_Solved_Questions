class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        mp = {}
        for i in range(n): mp[s[i]] = i
        r = 0
        res = []
        for i in range(n):
            r = max(r, mp[s[i]])
            if i==r: res.append(i+1)
        m = len(res)
        for i in range(m-1,0,-1):
            res[i] = res[i] - res[i-1]
        return res
        