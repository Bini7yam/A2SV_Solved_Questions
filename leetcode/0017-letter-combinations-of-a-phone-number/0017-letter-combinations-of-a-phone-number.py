class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {}
        s = ["abc",'def','ghi','jkl','mno','pqrs','tuv','wxyz']
        for i in range(2, 10):
            d[str(i)] = s[i - 2]
        rv = ['']
        for digit in digits:
            rv = [a + b for a in rv for b in d[digit]]
        return rv if digits else []
        