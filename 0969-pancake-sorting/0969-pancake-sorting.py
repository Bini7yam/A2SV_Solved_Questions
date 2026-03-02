class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        def flip(k):
            res.append(k)
            for i in range(k//2):
                j = k - 1 - i
                arr[i], arr[j] = arr[j], arr[i]
        for i in range(n,1,-1):
            j = arr.index(i)
            flip(j+1)
            flip(i)
        return res