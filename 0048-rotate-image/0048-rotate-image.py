class Solution:
    def rotate(self, mtx: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m=len(mtx),len(mtx[0])
        for i in range(n):
            for j in range(n):
                if i > j:continue
                mtx[i][j],mtx[j][i]=mtx[j][i],mtx[i][j]
        for i in range(n):
            for j in range(n):
                if j + j >= n:continue
                k = n - j - 1
                mtx[i][j],mtx[i][k]=mtx[i][k],mtx[i][j]
        
            