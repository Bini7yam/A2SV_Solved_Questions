class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        n1 = len(list1)
        n2 = len(list2)
        def find(x):
            res = []
            for i in range(n1):
                j = x-i
                if j < 0 or j >= n2:continue
                if list1[i] == list2[j]:res.append(list1[i])
            return res
        for x in range(n1+n2):
            arr = find(x)
            if arr: return arr