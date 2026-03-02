class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        a = 'abcdefghijklmnopqrstuvwxyz'
        pre = [0] * (n+1)
        for v in shifts:
            st,en,dr = v
            if dr:
                pre[st] += 1
                pre[en+1] -= 1
            else:
                pre[st]-=1
                pre[en+1]+=1
        c = 0
        t = ''
        for i in range(n):
            c += pre[i]
            c = (c%26 + 26) % 26
            j = a.index(s[i])
            k = (j+c) % 26
            t = t + a[k]
        return t
        