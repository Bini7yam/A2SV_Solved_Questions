class FrequencyTracker:
    def __init__(self):
        self.d = {}
        self.r = {}
        self.r[0] = 0

    def add(s, n: int) -> None:
        if n in s.d:
            s.r[s.d[n]] -= 1
            s.d[n] += 1
            if s.d[n] in s.r: s.r[s.d[n]] += 1
            else: s.r[s.d[n]] = 1
            
        else: 
            s.d[n] = 1
            if 1 in s.r: s.r[1] += 1
            else: s.r[1] = 1
        

    def deleteOne(s, n: int) -> None:
        if n in s.d and s.d[n]: 
            s.r[s.d[n]] -= 1
            s.d[n] -= 1
            s.r[s.d[n]] += 1
            
        

    def hasFrequency(s, f: int) -> bool:
        return f in s.r and s.r[f]!=0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)