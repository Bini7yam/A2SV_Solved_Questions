class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n,m =len(img), len(img[0])
        res = [[0]*m for i in range(n)]
        def val(i,j):
            return 0 <= i < n and 0 <= j < m
        for i in range(n):
            for j in range(m):
                itm = []
                for l in range(-1,2):
                    for r in range(-1,2):
                        ni,nj=i+l,r+j
                        if val(ni,nj): itm.append(img[ni][nj])
                res[i][j] = sum(itm)//len(itm)
        return res
                

        