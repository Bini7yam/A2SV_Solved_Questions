class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        cr,cm=[0]*26,[0]*26
        for c in r:cr[ord(c)-ord('a')]+=1
        for c in m:cm[ord(c)-ord('a')]+=1
        for i in range(26):
            if cr[i] > cm[i]:return False
        return True
        