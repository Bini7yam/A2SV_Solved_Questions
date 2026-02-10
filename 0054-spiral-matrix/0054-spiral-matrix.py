class Solution:
    def spiralOrder(self, mtx: List[List[int]]) -> List[int]:
        n = len(mtx)
        m = len(mtx[0])
        arr = []
        def go(u,d,l,r): 
            if u > d or l > r: return           
            if u==d and l==r:
                arr.append(mtx[u][l])
                return
            if u==d:
                for i in range(l,r+1):
                    arr.append(mtx[u][i])
                return
            if l==r:
                for i in range(u,d+1):
                    arr.append(mtx[i][l])
                return
            for i in range(l,r+1):
                arr.append(mtx[u][i])
            for j in range(u+1,d+1):
                arr.append(mtx[j][r])
            for i in range(r-1,l-1,-1):
                arr.append(mtx[d][i])
            for j in range(d-1,u,-1):
                arr.append(mtx[j][l])
            go(u+1,d-1,l+1,r-1)
        go(0,n-1,0,m-1)
        return arr
            
            
        