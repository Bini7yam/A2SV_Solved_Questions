class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        r=[]
        def bct(n,k,dummy=[]):
            if n<k:return
            if not k:r.append(dummy);return
            bct(n-1,k-1,dummy+[n])
            bct(n-1,k,dummy)
        bct(n,k)
        return r

        