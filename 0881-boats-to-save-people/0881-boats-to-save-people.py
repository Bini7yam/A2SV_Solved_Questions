class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        l = (n+1)//2
        r = ans = n
        def check(m):
            nonlocal n
            rmn = n - m
            r = rmn + rmn - 1
            for i in range(rmn):
                if people[i] + people[r] > limit: return False
                r -= 1
            return True
        while(l <= r):
            m = (l+r)//2
            if check(m):
                ans = m
                r = m-1
            else: l=m+1
        return ans
# 1 2 4 5