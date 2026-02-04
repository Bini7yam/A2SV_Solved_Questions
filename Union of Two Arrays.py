class Solution:    
    def findUnion(self, a, b):
        # code here
        sc = set()
        for x in a: sc.add(x)
        for x in b: sc.add(x)
        c = []
        for x in sc: c.append(x)
        return c
        
