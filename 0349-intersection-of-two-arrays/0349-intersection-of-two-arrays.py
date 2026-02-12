class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [i for i in range(1001) if i in nums1 and i in nums2]
        