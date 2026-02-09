class Solution:
    def firstUniqChar(self, s: str) -> int:
        ls = [0] * 26
        fs = [-1] * 26
        n = len(s)
        for i in range(n):
            v = ord(s[i])-ord('a')
            ls[v] = i
            fs[v] = i if fs[v]==-1 else fs[v]
        for i in range(n):
            v = ord(s[i])-ord('a')
            if ls[v]==i and fs[v]==i:return i
        return -1

        