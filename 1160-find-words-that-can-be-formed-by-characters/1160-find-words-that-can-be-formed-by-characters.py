class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        key = Counter(chars)
        res = 0
        for s in words:
            if Counter(s) <= key: res += len(s)
        return res
        