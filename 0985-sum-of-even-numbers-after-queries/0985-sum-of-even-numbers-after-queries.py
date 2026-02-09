class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sm = 0
        q = len(queries)
        res = []
        sm = sum(x for x in nums if x%2 == 0)
        for _ in range(q):
            v,i = queries[_]
            old = nums[i]
            if old % 2 == 0: sm -= old
            new = old + v
            if new % 2 == 0: sm += new
            res.append(sm)
            nums[i] = new
        return res

        