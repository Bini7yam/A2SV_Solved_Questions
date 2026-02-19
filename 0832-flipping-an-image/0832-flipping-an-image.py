class Solution:
    def flipAndInvertImage(self, img: List[List[int]]) -> List[List[int]]:
        n,m=len(img),len(img[0])
        return [[img[i][m-j-1]^1 for j in range(m)] for i in range(n)]
        