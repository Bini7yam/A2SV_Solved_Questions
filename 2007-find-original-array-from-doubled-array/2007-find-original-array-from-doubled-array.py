class Solution:
    def findOriginalArray(self, cd: List[int]) -> List[int]:
        n = int(1e5 + 15)
        cnt = [0] * n
        for x in cd: cnt[x] += 1
        if cnt[0]&1: return []
        res = [0] * (cnt[0]//2)
        for i in range(1,n):
            if not cnt[i]: continue
            if 2 * i >= n and cnt[i]:return []
            if cnt[i] > cnt[2*i]: return []
            res += [i]*cnt[i]
            cnt[i+i] -= cnt[i]
        return res
        