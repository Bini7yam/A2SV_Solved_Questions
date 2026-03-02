class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s = list(s)
        s.sort(key = lambda c:order.index(c) if c in order else 1000)
        return ''.join(s)
        