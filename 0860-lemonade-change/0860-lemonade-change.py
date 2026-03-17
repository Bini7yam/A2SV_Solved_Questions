class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5 = c10 = 0
        for bill in bills:
            x = bill
            if bill == 5:
                c5 += 1
                continue
            if bill == 10:
                if not c5: return False
                c5 -= 1
                c10 += 1
                continue
            if bill == 20:
                if c10:
                    bill -= 10
                    c10 -= 1
                    if not c5: return False
                    c5 -= 1
                else:
                    if c5 < 3: return False
                    c5 -= 3
        return True
        