class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 1
        cnt = allow = 0
        while maxDoubles and res*2 <= target:
            res += res
            maxDoubles -= 1
            cnt += 1
            allow += 1
        diff = target - res
        for i in range(30):
            if not (diff & 1<<i): continue
            if i <= allow: cnt += 1
            else: cnt += 1<<(i - allow)
        return cnt