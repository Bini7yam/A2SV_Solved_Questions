class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        los = [False] * n
        p = 0
        for i in range(1,n):
            c = 0
            while 1:
                c += not los[p]
                if c==k:break
                p += 1
                p %= n
            los[p] = 1
        for i in range(n):
            if not los[i]: return i+1

        