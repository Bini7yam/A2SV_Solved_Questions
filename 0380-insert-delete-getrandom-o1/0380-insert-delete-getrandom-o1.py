class RandomizedSet:
    def __init__(self):
        self.h = []
        self.chk = set()
        self.ins = set()

    def insert(self, val: int) -> bool:
        if val in self.chk: return False
        self.chk.add(val)
        if val not in self.ins:self.h.append(val)
        self.ins.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.chk: return False
        self.chk.remove(val)
        return True

    def getRandom(self) -> int:
        n = len(self.h)
        while True:
            i = randint(0,n-1)
            x = self.h[i]
            if x in self.chk:return x


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()