class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        t = n//3
        res = set()
        c = Counter(nums)
        for i in range(100):
            j = randint(0,n-1)
            x = nums[j]
            if c[x] > t: res.add(x)
        return list(res)
        