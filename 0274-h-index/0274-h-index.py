class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)
        res = 0
        for i in range(n):
            if citations[i] > i:
                res = i+1
        return res
        