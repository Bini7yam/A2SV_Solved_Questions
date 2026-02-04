class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        R = set()
        C = set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j]:continue
                R.add(i)
                C.add(j)
        for i in R:
            for j in range(c): matrix[i][j]=0
        for j in C:
            for i in range(r): matrix[i][j]=0
        
        