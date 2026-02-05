class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        plr = set()
        hst = {}
        for arr in matches:
            x,y = arr
            plr.add(x)
            plr.add(y)
            if y in hst: hst[y] += 1
            else: hst[y] = 1
        res = [[],[]]
        for x in plr:
            if x not in hst:res[0].append(x)
            elif hst[x]==1:res[1].append(x)
        res[0].sort()
        res[1].sort()
        return res

        