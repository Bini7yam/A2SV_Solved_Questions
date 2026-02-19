class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:(x[0],x[1]))
        print(points)
        right = -int(1e10)
        left = right
        res = 0
        for p in points:
            s,e = p
            if right < s:
                res += 1
                right = e
            else:
                right = min(right,e)
        return res
                
            