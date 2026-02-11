class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        a = sorted(nums)
        dom = a[n//2]
        f = a.count(dom)
        pre = 0
        for i in range(n-1):
            pre += nums[i]==dom
            post = f - pre
            l = i+1
            r = n-l
            if pre > l//2 and post > r//2: return i
        return -1