class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        back = '../'
        stay = './'
        for s in logs:
            if s == back: res -= 1
            elif s != stay: res += 1
            res = max(res,0)
        return res
        