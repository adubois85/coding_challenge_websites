class Solution:
    def isValid(self, s: str) -> bool:
        validity = True
        pairs = {')': '(',
                 '}': '{',
                 ']': '['}
        temp = []
        for i in s:
            if i in "({[":
                temp.append(i)
            elif not temp or pairs[i] != temp[-1]:
                validity = False
                return validity
            else:
                temp.pop()
        if temp:
            validity = False
        return validity
