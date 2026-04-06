class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        for x in nums:
            n = len(res)
            nls = []
            for i in range(n):
                if res[i][-1] > x: continue
                nr = res[i] + [x]
                fl = 1
                for r in res:
                    if r == nr: fl = 0
                for r in nls:
                    if r == nr: fl = 0
                if fl: nls.append(nr)
            res += nls
            res.append([x])
        return [x for x in res if len(x) > 1]