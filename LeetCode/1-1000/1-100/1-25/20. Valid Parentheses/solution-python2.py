class Solution:
    from collections import deque

    def isValid(self, s: str) -> bool:
        temp = deque()
        for i in s:
            if i in '({[':
                temp.append(i)
            elif not temp:
                return False
            else:
                if 1 <= ord(i) - ord(temp.pop()) <= 2:
                    pass
                else:
                    return False
        if temp:
            return False
        return True
