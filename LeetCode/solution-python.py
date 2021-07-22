from collections import deque
class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        deq = deque(s)
        while deq:
            x = romans[deq.popleft()]
            y = 0
            if x in {"I", "X", "C"} and 0 < (romans[deq[0]] - x) < (x * 10):
                x = x * -1
                y = romans[deq.popleft()]
            sum = sum + x + y
        return sum