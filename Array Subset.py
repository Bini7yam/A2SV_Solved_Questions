#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        da,db = {},{}
        for x in a:
            if x in da: da[x] += 1
            else: da[x] = 1
        for x in b:
            if x in db: db[x] += 1
            else: db[x] = 1
        for u,v in db.items():
            if u not in da: return False
            if da[u] < v: return False
        return True
    
    
    
    
