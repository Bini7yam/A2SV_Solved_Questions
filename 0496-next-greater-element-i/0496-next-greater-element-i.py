class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for x in nums1:
            i = 0
            while nums2[i]-x: i+=1
            res.append(-1)
            for j in range(i+1,len(nums2)):
                if nums2[j] > x:
                    res[-1] = nums2[j]
                    break
        return res