from typing import List


class Solution:
    # helper function to return the two's complement binary representation of
    # a number as a list of single character strings
    def twos_complement(n: List) -> List:
        n = list(f'{n:011b}')
        for i in range(len(n)):
            n[i] = ('0' if n[i] == '1' else '1')
        # bin_add(n, 1)
        return n


    def getSum(self, a: int, b: int) -> int:
        pass
