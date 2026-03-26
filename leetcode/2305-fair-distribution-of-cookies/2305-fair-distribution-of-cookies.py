class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        average = sum(cookies)/k
        dist = [0] * k
        mx = 10000000
        def dfs(i):
            if i==n: return max(dist)
            res = mx
            for j in range(k):
                if dist[j] > average or dist[j] + cookies[i] > res: continue
                dist[j] += cookies[i]
                res = min(res, dfs(i+1))
                dist[j] -= cookies[i]
            return res

        return dfs(0)





            