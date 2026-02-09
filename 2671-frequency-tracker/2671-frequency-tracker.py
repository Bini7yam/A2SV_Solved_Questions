class FrequencyTracker:
    def __init__(self):
        self.d = {}

    def add(s, n: int) -> None:
        if n in s.d:s.d[n] += 1
        else: s.d[n] = 1
        

    def deleteOne(s, n: int) -> None:
        if n in s.d and s.d[n]: s.d[n] -= 1
        

    def hasFrequency(s, f: int) -> bool:
        return f in s.d.values()
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)