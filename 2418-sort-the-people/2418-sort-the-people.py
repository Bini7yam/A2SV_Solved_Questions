class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        ind = [i for i in range(n)]
        for i in range(n):
            for j in range(1,n):
                if heights[ind[j-1]] < heights[ind[j]]:
                    ind[j],ind[j-1]=ind[j-1],ind[j]
        return [names[i] for i in ind]
        