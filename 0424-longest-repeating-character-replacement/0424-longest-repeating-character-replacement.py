class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def find(c):
            nonlocal k,s
            n = len(s)
            diff = l = res = 0
            for i in range(n):
                diff += s[i] != c
                while diff > k:
                    diff -= s[l] != c
                    l += 1
                res = max(res, i - l + 1)
            return res
        res = 0
        a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(26):
            res = max(res, find(a[i]))
        return res