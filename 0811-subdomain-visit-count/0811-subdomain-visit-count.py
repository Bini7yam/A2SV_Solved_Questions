class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        def pro(s):
            num, dmn = s.split()
            num = int(num)
            dmn = '.'+dmn
            n = len(dmn)
            for i in range(n):
                if dmn[i] != '.':continue
                sdmn = dmn[i+1:]
                if sdmn in d:d[sdmn]+=num
                else:d[sdmn]=num
        for s in cpdomains:pro(s)
        return [str(x)+' '+nm for nm,x in d.items()]
        