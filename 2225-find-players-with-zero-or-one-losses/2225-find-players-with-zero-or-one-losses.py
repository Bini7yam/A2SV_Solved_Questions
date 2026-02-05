class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        loss = {}
        for arr in matches:
            w,l = arr
            players.add(w)
            players.add(l)
            if l in loss: loss[l] += 1
            else: loss[l] = 1
        res = [[],[]]
        for x in players:
            if x not in loss:res[0].append(x)
            elif loss[x]==1:res[1].append(x)
        res[0].sort()
        res[1].sort()
        return res

        