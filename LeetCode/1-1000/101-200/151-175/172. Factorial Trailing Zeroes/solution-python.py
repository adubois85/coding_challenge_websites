from math import factorial


class Solution:
    def trailingZeroes(self, n: int) -> int:
        # LOL brute-force
        # but yes, there's a better way
        if n < 5:
            return 0
        f = factorial(n)
        counter = 0
        while f % (10 ** (counter + 1)) == 0:
            counter += 1
        return counter
