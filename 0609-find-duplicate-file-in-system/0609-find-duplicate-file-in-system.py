class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        arr = []
        def change(s):# directory, 
            i = 0
            while s[i] != ' ': i += 1
            drt = s[:i]
            s = s[i+1:]
            for t in s.split(' '):
                i = 0
                while t[i]!='(':i+=1
                name = t[:i]
                message = t[i+1:-1]
                arr.append([message,name,drt])
        
        for s in paths:change(s)
        arr.sort(key=lambda x:x[0])
        key = '#!%$@'
        res = []
        for data in arr:
            msg,name,drt = data
            if msg != key:
                key = msg
                res.append([drt+'/'+name])
            else: res[-1].append(drt+'/'+name)
        return [sl for sl in res if len(sl) > 1]


        