class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        d={}
        ma=[]
        for num in nums:
            if num in d: d[num]+=1
            else: d[num]=1
        r = [[]]
        for key, value in d.items():
            # print(key,value)
            temp = list(r)
            for i in range(1,value + 1):
                r += [([key] * i) + j for j in temp]
        return r
        
        