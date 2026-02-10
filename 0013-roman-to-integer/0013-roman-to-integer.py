class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        n = 0
        sym = 'IVXLCDM'
        val = [1,5,10,50,100,500,1000]
        while s:
            if len(s)==1:
                n += val[sym.index(s)]
                break
            t = s[:2]
            if t=='IV':n += 4
            elif t=='IX': n += 9    
            elif t=='XL':n += 40
            elif t=='XC':n+=90
            elif t=='CD':n+=400
            elif t=='CM':n+=900
            else:
                n += val[sym.index(s[0])]
                s = s[1:]
                continue
            s = s[2:]
        return n

        