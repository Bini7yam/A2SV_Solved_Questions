class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1,c2=[0]*26,[0]*26
        for c in word1: c1[ord(c)-ord('a')]+=1
        for c in word2: c2[ord(c)-ord('a')]+=1
        return sorted(c1)==sorted(c2)
        