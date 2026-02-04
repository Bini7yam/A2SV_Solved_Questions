class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort(key=lambda x:x[0])
        n = len(ranges)
        p = 0
        while p < n and ranges[p][1] < left: p += 1
        if p==n or ranges[p][0] > left: return False
        lr = ranges[p][0]
        for i in range(p,n):
            l,r = ranges[i]
            if l > lr+1: return False
            lr = max(lr,r)
            if lr >= right: return True
        return False
