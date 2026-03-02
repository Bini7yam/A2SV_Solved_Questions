class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)//3
        piles.sort()
        return sum(piles[i] for i in range(n,3*n,2))
        