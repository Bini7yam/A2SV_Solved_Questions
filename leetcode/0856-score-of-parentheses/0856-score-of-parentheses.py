class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def dfs(s):
            n = len(s)
            if not n: return 0
            if n==2: return 1
            cnt = 1
            t = ''
            for i in range(1,n):
                if s[i] == '(': cnt += 1
                else: cnt -= 1
                if not cnt:
                    return max(1,2 * dfs(t)) + dfs(s[i+1:])
                t = t + s[i]
        return dfs(s)
        