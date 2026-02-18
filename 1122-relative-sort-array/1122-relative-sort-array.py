class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n1,n2 = len(arr1), len(arr2)
        pos_in_arr2 = [0] * 1005
        in_arr2 = [False] * 1005
        for i in range(n2):
            x = arr2[i]
            pos_in_arr2[ x ] = i
            in_arr2[ x ] = True
        offset = 2000
        def order(x):
            return pos_in_arr2[x] if in_arr2[x] else offset + x
        arr1.sort(key = order)
        return arr1
        