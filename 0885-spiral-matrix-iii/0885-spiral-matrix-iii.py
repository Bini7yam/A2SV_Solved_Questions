class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rs: int, cs: int) -> List[List[int]]:
        vs = set()
        dr = [(-1,0),(0,1),(1,0),(0,-1)]
        d = 0
        res = []
        def add(p, i):
            return [p[0] + dr[i][0], p[1] + dr[i][1]]
        def id(p):
            i,j=p
            return i*1000000 + j
        cur = [rs,cs]
        vs.add(id(cur))
        def inb(p):
            i,j=p
            return 0 <= i < rows and 0 <= j < cols
        while len(res) < rows * cols:
            print(cur,d)
            if inb(cur): res.append(cur)
            nd = (d+1) % 4
            nx = add(cur, nd)
            if id(nx) in vs:
                nd = d
                nx = add(cur, nd)
            cur = nx
            d = nd
            vs.add(id(cur))
        return res

