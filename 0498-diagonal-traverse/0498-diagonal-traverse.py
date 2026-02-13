class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row, column = len(mat), len(mat[0])
        up = (-1, 0)
        down = (1, 0)
        left = (0, -1)
        right = (0, 1)
        dup = (-1, 1)
        ddown = (1, -1)
        d = 1
        def next(pos):
            nonlocal d
            if d:
                if pos[1] == column - 1:
                    d = 0
                    return add(pos, down)
                if pos[0] == 0:
                    d = 0
                    return add(pos, right)
                return add(pos, dup)
            if pos[0] == row - 1:
                d = 1
                return add(pos,right)
            if pos[1] == 0:
                d = 1
                return add(pos, down)
            return add(pos, ddown) 
        def inbound(a):
            return a[0] >= 0 and a[1] >= 0 and a[0] < row and a[1] < column
        cur = (0,0)

        def add(a, b):
            return(a[0] + b[0], a[1] + b[1])
        def at(grid, a):
            return grid[a[0]][a[1]]
        rv = []
        for i in range(row * column):
            print(i, cur, d)
            rv.append(at(mat, cur))
            cur = next(cur)
            if not i: print(cur)
        return rv
            

        