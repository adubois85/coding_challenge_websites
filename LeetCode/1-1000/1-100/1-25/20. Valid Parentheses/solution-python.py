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
            elif pairs[i] not in temp:
                validity = False
                return validity
            else:
                temp.remove(pairs[i])
        if temp:
            validity = False
        return validity
