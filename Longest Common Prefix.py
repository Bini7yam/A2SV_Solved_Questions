class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = 0
        while all(len(s)>l and s[l]==strs[0][l] for s in strs): l+=1
        return strs[0][:l]
        
