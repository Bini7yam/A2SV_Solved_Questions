class Solution:
    def countGoodNumbers(self, n: int) -> int:
        oexp = n//2
        eexp = (n+1)//2
        res = 1
        bo = 4
        MOD = int(1e9 + 7)
        while oexp:
            if oexp & 1: res = res * bo % MOD
            bo  = bo * bo % MOD
            oexp>>=1
        be = 5
        while eexp:
            if eexp & 1: res = res* be % MOD
            be = be * be % MOD
            eexp>>=1
        return res