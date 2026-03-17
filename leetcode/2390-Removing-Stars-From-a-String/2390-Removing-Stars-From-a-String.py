class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack:
                stack = [c]
                continue
            if c != '*' or stack[-1]=='*':
                stack.append(c)
            else: stack.pop()
        return ''.join(stack)