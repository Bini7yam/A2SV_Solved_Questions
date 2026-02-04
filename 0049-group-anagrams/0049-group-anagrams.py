class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort(key = lambda x:sorted(x))
        res = []
        n = len(strs)
        i = 0
        arr = []
        ls = sorted(strs[0])
        #print(strs)
        while(i < n):
            while i < n and sorted(strs[i])==ls:
                arr.append(strs[i])
                i += 1
            
            res.append(arr.copy())
            arr = []
            if i==n:break
            ls = sorted(strs[i])
        return res
        