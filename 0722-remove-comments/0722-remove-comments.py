class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        def tr(s):
            r = ""
            ls = 0
            while s.find('/*',ls)+1 or s.find('//',ls)+1:
                p = s.find('/*',ls)
                w = s.find('//',ls)
                if w != -1 and (p==-1 or w < p): 
                    r += s[ls:w]
                    return [r,False]
                r += s[ls:p]
                q = s.find('*/',p+2)
                if q==-1:
                    return [r,True]
                ls = q + 2
            r += s[ls:]
            return [r, False]
        mop = False
        res = []
        for s in source:
            if mop:
                x = s.find('*/')
                if x==-1:continue
                s = s[x+2:]
                t,mop = tr(s)
                if t:res[-1]+=t
                continue
            t,mop = tr(s)
            if t:res.append(t)
            continue
        return res
            

        