class Solution:
    def findDiagonalOrder(self, mtx: List[List[int]]) -> List[int]:
        d = [-1,1]
        pos = [0,0]
        n,m=len(mtx),len(mtx[0])
        res = [mtx[0][0]]
        def nx(pos):
            i,j=pos
            return [i+d[0], j+d[1]]
        def val(pos):
            i,j=pos
            return 0<=i<n and 0<=j<m
        for _ in range(1,n*m):
            i,j = pos
            np = nx(pos)
            if not val(np):
                d[0] *= -1
                d[1] *= -1
                if j==m-1: i+=1
                elif not i: j+=1
                elif i==n-1: j+=1
                else: i+=1
                np = [i,j]
            i,j=np
            res.append(mtx[i][j])
            pos=[i,j]
        return res
            

            

        
