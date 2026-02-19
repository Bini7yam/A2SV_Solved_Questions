class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        def flip(k):
            res.append(k)
            for i in range(k//2):
                j = k - 1 - i
                arr[i],arr[j]=arr[j],arr[i]
        flip(arr.index(1)+1)
        for i in range(2,n):
            flip(n)
            x = arr.index(i)
            flip(x+1)
            flip(n-i+1)
            flip(n)
        return res
        