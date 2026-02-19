class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rot():
            nonlocal mat
            mat = [list(l) for l in zip(*mat)]
            n,m=len(mat),len(mat[0])
            for i in range(n):
                for j in range(m//2):
                    k = m - j - 1
                    mat[i][j],mat[i][k]=mat[i][k],mat[i][j]
        for i in range(4):
            if mat==target:return True
            rot()
        return False
        