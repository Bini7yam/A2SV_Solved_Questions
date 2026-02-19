class Solution:
    def smallestPalindrome(self, s: str) -> str:
        odd = ''
        alp = 'abcdefghijklmnopqrstuvwxyz'
        cnt = [0] * 26
        for c in s: cnt[ord(c)-ord('a')]+=1
        l = r = ''
        for i in range(26):
            c = alp[i]
            if cnt[i]&1: odd = c
            md = cnt[i]//2
            l = l + c * md
            r= c * md + r
        return l + odd + r
        