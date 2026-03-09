class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {}
        pair['(']=')'
        pair['[']=']'
        pair['{']='}'
        pair['}']=''
        pair[')']=''
        pair[']']=''
        for c in s:
            if not stack: 
                stack.append(c)
                continue
            if pair[stack[-1]] == c:stack.pop()
            else: stack.append(c)
        return not stack