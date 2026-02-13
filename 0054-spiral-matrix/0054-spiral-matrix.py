class Solution:
    def spiralOrder(self, mtx: List[List[int]]) -> List[int]:
        n,m=len(mtx),len(mtx[0])
        d = [[0,1],[1,0],[0,-1],[-1,0]]
        dc = 0
        vs = [[False]*m for i in range(n)]
        vs[0][0]=1
        pos = [0,0]
        res = [mtx[0][0]]
        def val(pos):
            i,j=pos
            return 0<=i<n and 0<=j<m and not vs[i][j]
        def add(p,q):
            return [p[0]+q[0],p[1]+q[1]]
        for _ in range(1,n*m):
            if not val(add(pos,d[dc])): dc = (dc+1)%4
            pos = add(pos,d[dc])
            i,j=pos
            res.append(mtx[i][j])
            vs[i][j]=1
        return res
                
                
            
