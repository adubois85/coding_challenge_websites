from typing import List
"""
Doing things the hard way
How to add two numbers together without using plus or minus signs
The only minus signs are in the arrows for the type annotations
I even took them out of the comments to drive the point home
Why they ever thought this was an 'easy' problem I'll never know
"""


class Solution:
    def bin_add(self, m: List, n: List) -> List:
        # Helper function to add two binary numbers of equal lengths as
        # represented by a list of individual strings
        # Dictionary mapping all possible combinations of both numbers' bits
        # and carry bit to the resultant bit and carry bit values as a bunch of
        # tuples.  Should make things quicker and easier I hope.
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
        # reversing both so I can use the length of a number for the iterator;
        # if I tried to go through each in reverse order (e.g. m[negative i]),
        # I'd have to add 1 to the length to hit every index.  Either that or
        # hard code the value, which is bad in a different way
        m, n = list(reversed(m)), list(reversed(n))
        for i in range(len(m)):
            temp = (m[i], n[i], carry)
            summed.append(mappings[temp][0])
            carry = mappings[temp][1]
        return list(reversed(summed))

    def twos_complement(self, n: List) -> List:
        # Helper function to return the two's complement binary representation
        # of a number as a list of single character strings
        n = self.invert_bits(n)
        return self.bin_add(n, list(f'{1:011b}'))

    def invert_bits(self, n: List) -> List:
        # Helper function to invert the bits (bitwise NOT) of a binary number
        # as represented by a list of single character strings
        for i in range(len(n)):
            n[i] = ('0' if n[i] == '1' else '1')
        return n

    def getSum(self, a: int, b: int) -> int:
        # need to pass the absolute value for negative numbers, otherwise the
        # left most digit will be a minus sign instead of a 0 or 1
        a = (self.twos_complement(list(f'{abs(a):011b}')) if a < 0 else list(f'{a:011b}'))
        b = (self.twos_complement(list(f'{abs(b):011b}')) if b < 0 else list(f'{b:011b}'))
        a = self.bin_add(a, b)
        # in two's complement, the left most digit is the sign bit
        # negative numbers will have a 1 and need to be reinverted
        # positive numbers and 0 will have a 0
        if a[0] == '1':
            a = ''.join(self.invert_bits(a))
            # bitwise NOT; was the only way I could think of to get a minus
            # sign without writting it out (e.g. a * (negative 1))
            return ~int(a, 2)
        return int(''.join(a), 2)
