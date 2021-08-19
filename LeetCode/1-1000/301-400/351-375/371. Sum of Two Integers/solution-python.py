from typing import List


class Solution:
    def bin_add(self, m: List, n: List) -> List:
        # helper function to add two binary numbers of equal lengths as
        # represented by a list of individual strings
        mappings = {('0', '0', 0): ('0', 0),
                    ('1', '0', 0): ('1', 0),
                    ('0', '1', 0): ('1', 0),
                    ('0', '0', 1): ('1', 0),
                    ('1', '1', 0): ('0', 1),
                    ('1', '0', 1): ('0', 1),
                    ('0', '1', 1): ('0', 1),
                    ('1', '1', 1): ('1', 1)}
        summed = []
        carry = 0
        m, n = list(reversed(m)), list(reversed(n))
        for i in range(len(m)):
            temp = (m[i], n[i], carry)
            summed.append(mappings[temp][0])
            carry = mappings[temp][1]
        return list(reversed(summed))

    def twos_complement(self, n: List) -> List:
        # helper function to return the two's complement binary representation
        # of a number as a list of single character strings
        n = list(f'{n:011b}')
        for i in range(len(n)):
            n[i] = ('0' if n[i] == '1' else '1')
        self.bin_add(n, list(f'{1:011b}'))
        return n

    def getSum(self, a: int, b: int) -> int:
        pass
