class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        inf=float("inf")
        n=len(cookies)
        avg=sum(cookies)/k
        track=[0]*k
        def bct(i=0,ma=0):
            if i==n:return ma
            mi=inf
            for j in range(k):
                if track[j]>avg or track[j]+cookies[j]>mi:continue
                track[j]+=cookies[i]
                nma=max(ma,track[j])
                mi=min(mi,bct(i+1,nma))
                track[j]-=cookies[i]
            return mi
        return bct()



        