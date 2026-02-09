class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        off = -min(nums)
        n = len(nums)
        if off>0:
            for i in range(n):nums[i] += off
        cnt = [0] * (max(nums) + 1)
        for x in nums: cnt[x] += 1
        ind = [i for i in range(len(cnt))]
        ind.sort(key=lambda x:-cnt[x])
        return [x - max(0,off) for x in ind[:k]]
        