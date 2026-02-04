class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        a.sort()
        b.sort()
        n,m = len(a),len(b)
        if n-m: return False
        for i in range(n):
            if a[i] - b[i]: return False
        return True
